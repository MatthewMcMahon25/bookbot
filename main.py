from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt") 
    print(book_text)

    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

main()