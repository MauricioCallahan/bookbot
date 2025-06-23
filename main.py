from stats import number_of_words
from stats import number_of_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = "/home/mauri/bookbot/books/frankenstein.txt"

    text = get_book_text(filepath)

    print(f"""
        ============ BOOKBOT ============
        Analyzing book found at {filepath}...
        ----------- Word Count ----------
        Found {number_of_words(text)} total words
        --------- Character Count -------
        {number_of_characters(text)}


    """)

if __name__ == '__main__':
    main()