# Riley Ahlrichs    4-27-15
# Lab Week 14: ChimpRefractor.py, learining how to use pygame-ce to update code for chimp.py and create a new class to
# practice inheritance. 

#!/usr/bin/env python
"""pygame.examples.chimp

This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation,
follow along in the tutorial.
"""

# Import Modules
import os
import pygame

if not pygame.font:
    print("Warning, fonts disabled")
if not pygame.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")


class Entity(pygame.sprite.Sprite):
    def __init__(self, image_name, colorkey=None, scale=None, data_dir=None):
        # Initialize the parent class (Sprite)
        super().__init__()

        # Ensure data_dir is provided
        if data_dir is None:
            raise ValueError("data_dir must be provided for loading resources.")

        # Construct the full path for the image
        image_path = os.path.join(data_dir, image_name)

        # Load the image
        self.image = pygame.image.load(image_path)

        # If a colorkey is provided, apply it for transparency
        if colorkey is not None:
            self.image.set_colorkey(colorkey)

        # If a scale is provided, scale the image
        if scale:
            self.image = pygame.transform.scale(self.image, scale)

        # Get the rectangle for positioning the sprite
        self.rect = self.image.get_rect()

# Define a dummy sound class to return when the file is missing
class NoneSound:
    def play(self):
        pass  # Do nothing when play is called

def load_sound(filename):
    """Load a sound file, with error handling for missing files."""
    try:
        sound = pygame.mixer.Sound(filename)
        return sound
    except pygame.error as e:
        print(f"Error loading sound '{filename}': {e}")
        # Return a dummy NoneSound object if the sound can't be loaded
        return NoneSound()


# classes for our game objects
class Fist(Entity):
    """Moves a clenched fist on the screen, following the mouse"""
    def __init__(self, image_name="fist.png", colorkey=None, scale=None, data_dir=None):
        # Initialize the parent Entity class and pass data_dir
        super().__init__(image_name, colorkey, scale, data_dir)

        # Initialize fist-specific attributes
        self.fist_offset = (-235, -80)
        self.punching = False

    def update(self):
        """Move the fist based on the mouse position"""
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punching:
            self.rect.move_ip(15, 25)

    def punch(self, target):
        """Returns true if the fist collides with the target"""
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """Called to pull the fist back"""
        self.punching = False

class Chimp(Entity):
    """Moves a monkey critter across the screen. It can spin the monkey when it is punched."""

    def __init__(self, image_name="chimp.png", colorkey=None, scale=None, data_dir=None):
        # Initialize the parent Entity class and pass data_dir
        super().__init__(image_name, colorkey, scale, data_dir)

        # Initialize chimp-specific attributes
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 90
        self.move = 18
        self.dizzy = False
        self.original = self.image  # Store the original image for spinning

    def update(self):
        """Walk or spin, depending on the monkey's state"""
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        """Move the monkey across the screen, and turn at the ends"""
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pygame.transform.flip(self.image, True, False)
        self.rect = newpos

    def _spin(self):
        """Spin the monkey image"""
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = False
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        """This will cause the monkey to start spinning"""
        if not self.dizzy:
            self.dizzy = True
            self.original = self.image

def main():
    """this function is called when the program starts.
    it initializes everything it needs, then runs in
    a loop until the function returns."""
    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((1280, 480), pygame.SCALED)
    pygame.display.set_caption("Monkey Fever")
    pygame.mouse.set_visible(False)

    if not pygame.font:
        print("Warning, fonts disabled")
    if not pygame.mixer:
        print("Warning, sound disabled")

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")

    # Create The Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Put Text On The Background, Centered
    font = pygame.Font(None, 64)
    text = font.render("Pummel The Chimp, And Win $$$", True, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
    background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    whiff_sound = load_sound(os.path.join(data_dir, "whiff.wav"))
    punch_sound = load_sound(os.path.join(data_dir, "punch.wav"))
    chimp = Chimp(image_name="chimp.png", colorkey=(255, 0, 0), scale=(200, 200), data_dir=data_dir)
    fist = Fist(image_name="fist.png", colorkey=(0, 38, 255), scale=(250, 250), data_dir=data_dir)
    all_sprites = pygame.sprite.Group(chimp, fist)
    clock = pygame.Clock()

    # Main Loop
    going = True
    while going:
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                going = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()  # punch
                    chimp.punched()
                else:
                    whiff_sound.play()  # miss
            elif event.type == pygame.MOUSEBUTTONUP:
                fist.unpunch()

        all_sprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
# Game Over

# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()