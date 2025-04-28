# Riley Ahlrichs        4-4-2025
# Lab 11: This program analyzes the word frequency of a cleaned text file (book) from Project Gutenberg.
# It counts how many times each word appears, and writes the sorted results to a new file.

import os

def analyzeBook(filename):
    count = {}

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                # Remove common punctuation
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", '')
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')
                # Convert to lowercase
                word = word.lower()
                # Only count alphabetic words (ignore numbers and symbols)
                if word.isalpha():
                    count[word] = count.get(word, 0) + 1

    return count

def outputAnalysis(count_dict, filename):
    # Create output filename: <title>_analysis.txt
    title, _ = os.path.splitext(filename)
    output_filename = f"{title}_analysis.txt"

    with open(output_filename, 'w', encoding='utf-8') as out_file:
        for word in sorted(count_dict.keys()):
            out_file.write(f"{word} {count_dict[word]}\n")

    print(f"Word analysis saved to: {output_filename}")


def main():
    filename = input("Enter the name of the .txt file (e.g., alice.txt): ").strip()

    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return

    word_counts = analyzeBook(filename)
    outputAnalysis(word_counts, filename)

if __name__ == "__main__":
    main()