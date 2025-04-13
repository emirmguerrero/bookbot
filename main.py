import sys
from stats import get_num_words
from stats import get_char_count
from stats import sorted_count

def main():

    try:
        file_path = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    num_words = get_num_words(file_path)
    num_char = get_char_count(file_path)
    sorted_list = sorted_count(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')

    print("--------- Character Count -------")
    for i in sorted_list:
        if i["letter"].isalpha():
            print(f'{i["letter"]}: {i["num"]}')

    print("============= END ===============")

main()