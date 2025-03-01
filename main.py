def main():
  frankenstein_path = "books/frankenstein.txt"
  frankenstain_content = get_book_text(frankenstein_path)

  # print(frankenstain_content)
  print(f"{count_words(frankenstain_content)} words found in the document")
  
def get_book_text(file_to_path):
  with open(file_to_path) as f:
    return f.read()

def count_words(text):
  text_array = text.split()
  return len(text_array)
  
main()
