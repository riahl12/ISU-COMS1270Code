# Riley Ahlrichs        4-4-2025
# Lab 11: This script reads a file, removes non-ASCII characters from its contents,
# and writes the cleaned content to a new file with "_clean" added to the filename.

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return ""

def removeNonASCII(text):
    clean = ""
    for char in text:
        if ord(char) < 128:  # ASCII characters are in the range 0-127
            clean += char
    return clean

def write_clean_file(original_filename, cleaned_text):
    # Create the new filename by appending '_clean' before the extension
    if '.' in original_filename:
        name_parts = original_filename.rsplit('.', 1)
        new_filename = f"{name_parts[0]}_clean.{name_parts[1]}"
    else:
        new_filename = original_filename + "_clean"

    with open(new_filename, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)
    
    print(f"Cleaned file written to: {new_filename}")

def main():
    filename = input("Enter the name of the .txt file: ")

    file_contents = read_file(filename)
    cleaned_contents = removeNonASCII(file_contents)
    write_clean_file(filename, cleaned_contents)

if __name__ == "__main__":
    main()
