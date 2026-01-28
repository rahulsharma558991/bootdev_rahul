from stats import get_num_words, get_num_characters, get_sorted_list_of_dicts
import sys

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    get_num_char = get_num_characters(text)
    word_count = get_num_words(text)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    res = get_sorted_list_of_dicts(get_num_char)
    for item in res:
        print(f"{item['char']}: {item['num']}")
    print(f"============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()