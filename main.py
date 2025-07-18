import sys
from stats import get_num_words, get_character_counts, get_sorted_dictionaries

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # Input command line book argument
    book_text = get_book_text(sys.argv[1]) 
    num_words = get_num_words(book_text)
    character_counts = get_character_counts(book_text)
    sorted_dictionaries = get_sorted_dictionaries(character_counts)

    print("============ BOOKBOT ============")
    # Input command line book argument
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item_dict in sorted_dictionaries:
            if item_dict["char"].isalpha():
                 print(f"{item_dict["char"]}: {item_dict["num"]}")
    print("============= END ===============")

if len(sys.argv) != 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

main()