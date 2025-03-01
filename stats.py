def count_words(text):
  text_array = text.split()
  return len(text_array)

def count_chars(text):
  char_count = {}
  text_lowered = text.lower()
  
  for char in text_lowered:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  
  return char_count
