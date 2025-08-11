import sys


def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

from stats import get_num_words
from stats import get_chars_dict
from stats import chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        x = get_book_text(sys.argv[1])
        y = get_num_words(x)
        z = get_chars_dict(x)
        a = chars_dict_to_sorted_list(z)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {y} total words")
        print("--------- Character Count -------")
        for item in a:
            if item["char"].isalpha():
                    print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
main()