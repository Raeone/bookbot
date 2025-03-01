from stats import count_words
from stats import count_chars 
from stats import sorted_chars

def main():
  frankenstein_path = "books/frankenstein.txt"
  frankenstein_content = get_book_text(frankenstein_path)
  chars_dict = count_chars(frankenstein_content)
  sorted_characters = sorted_chars(chars_dict)

  # print(frankenstein_content)
  # print(f"{count_words(frankenstein_content)} words found in the document")
  # print(count_chars(frankenstein_content))
  # print(sorted_characters)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {frankenstein_path}...")
  print("----------- Word Count ----------")
  print(f"Found {count_words(frankenstein_content)} total words")
  print("--------- Character Count -------")
  
  for char in sorted_characters:
    for key in char:
      if key.isalpha():
        print(f"{key}: {char[key]}")

  print("============= END ===============")



  
def get_book_text(file_to_path):
  with open(file_to_path) as f:
    return f.read()


  
main()
