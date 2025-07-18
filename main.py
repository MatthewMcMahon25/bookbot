from stats import get_num_words, get_character_counts, get_sorted_dictionaries

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt") 
    num_words = get_num_words(book_text)
    character_counts = get_character_counts(book_text)
    sorted_dictionaries = get_sorted_dictionaries(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item_dict in sorted_dictionaries:
            if item_dict["char"].isalpha():
                 print(f"{item_dict["char"]}: {item_dict["num"]}")
    print("============= END ===============")

main()