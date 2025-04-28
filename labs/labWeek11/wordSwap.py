# Riley Ahlrichs        4-4-2025
# Lab 11: Replaces each unique word in a sentence with another randomly selected word.

import random

def build_swap_dict(words):
    swap_dict = {}
    for word in set(words):  # use unique keys only
        swap_dict[word] = random.choice(words)  # random word from the original list
    return swap_dict

def swap_sentence(words, swap_dict):
    return [swap_dict[word] for word in words]

def main():
    sentence = input("Enter a Sentence: ")
    words = sentence.split()
    
    swap_dict = build_swap_dict(words)

    print(swap_dict)

    swapped = swap_sentence(words, swap_dict)
    print(" ".join(swapped))

if __name__ == "__main__":
    main()
