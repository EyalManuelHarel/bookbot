import sys
from stats import count_words, sort_dict

# returns the contents of the file as str
def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file_path = f"./{sys.argv[1]}"
    frankenstein_text = get_book_text(book_file_path)
    unique_words_count = count_words(frankenstein_text)
    unique_chars_count = sort_dict(frankenstein_text)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_file_path}
----------- Word Count ----------
Found {unique_words_count} total words
--------- Character Count -------""")
    for char, value in unique_chars_count:
        if char.isalpha():
            print(f"{char}: {value}")
    # print(print_report(unique_chars_count), sep='\n')
main()