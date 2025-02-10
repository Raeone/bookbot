def main():
  book_path = "books/frankenstein.txt"
  book_content = get_file_content(book_path)
  # print(book_content)
  print(count_words(book_content))

def get_file_content(path):
  with open(path) as file:
    return file.read()

def count_words(text):
  text_arr = text.split()
  return len(text_arr)






main()
