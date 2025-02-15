def main():
  book_path = "books/frankenstein.txt"
  book_content = get_file_content(book_path)
  number_of_chars = count_chars(book_content)
  # print(book_content)
  # print(count_words(book_content))
  print(number_of_chars)

def get_file_content(path):
  with open(path) as file:
    return file.read()

def count_words(text):
  text_arr = text.split()
  return len(text_arr)

def count_chars(text):
  chars = {}
  
  for char in text:
    lowered = char.lower()

    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1

  return chars


main()
