import sys
from stats import count_words, count_letters, sort_dict

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_contents = get_books_text(file_path)
    word_count = count_words(file_contents)
    letter_counts = count_letters(file_contents)
    print_report(file_path, word_count, letter_counts)

def print_report(file_path, word_count, letter_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for kvp in letter_counts:
        letter = kvp["char"]
        if not letter.isalpha():
            continue

        count = kvp["num"]
        print(f"{letter}: {count}")
    print("============= END ===============")

def get_books_text(file_path):
    with open(file_path) as f:
        return f.read()

main()

