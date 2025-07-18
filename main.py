def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count(text):
    # Split the string into a list of strings
    text_list = text.split()

    # return length of list
    return len(text_list)


def main():
    book_text = get_book_text("books/frankenstein.txt") 
    print(book_text)

    num_words = count(book_text)
    print(f"{num_words} words found in the document")

main()