import sys
from stats import (
  count_words,
  chars_dict,
  chars_dict_to_sorted_list
)

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]
  book_content = get_book_text(book_path) # string
  num_of_words = count_words(book_content) # number
  num_of_chars = chars_dict(book_content) # dict
  sorted_num_of_chars = chars_dict_to_sorted_list(num_of_chars) # list of dicts

  print_report(book_path, num_of_words, sorted_num_of_chars)


def get_book_text(file_to_path):
  """Load content of a file.

  Args:
      file_to_path (string): url path to file to be load

  Returns:
      string: content of the file
  """
  with open(file_to_path) as f:
    return f.read()


def print_report(book_path, words_count, characters_list):
  """Print report and statistics from a book

  Args:
      book_path (string): url path  
      words (number): count of words in book
      characters_list (dictionary): dictionary of characters and counts
  """
  
  print("\n============ BOOKBOT ============\n")
  print(f"Analyzing book found at {book_path}...")
  print("\n----------- Word Count ----------\n")
  print(f"Found {words_count} total words")
  print("\n--------- Character Count -------\n")
  
  for char in characters_list:
    for key in char:
      if key.isalpha():
        print(f"{key}: {char[key]}")

  print("============= END ===============")


main()
