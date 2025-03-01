from stats import count_words 

def main():
  frankenstein_path = "books/frankenstein.txt"
  frankenstein_content = get_book_text(frankenstein_path)

  # print(frankenstein_content)
  print(f"{count_words(frankenstein_content)} words found in the document")
  
def get_book_text(file_to_path):
  with open(file_to_path) as f:
    return f.read()


  
main()
