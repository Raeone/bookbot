def main():
  frankenstein_path = "books/frankenstein.txt"
  print(get_file_content(frankenstein_path))

def get_file_content(path):
  with open(path) as file:
    return file.read()




main()
