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

def sort_on(dict):
  for key in dict:
    return(dict[key])
  
def sorted_chars(dictionary_of_chars):
  chars_arr = []

  for key in dictionary_of_chars:
    chars_arr.append({key: dictionary_of_chars[key] })

  chars_arr.sort(key=sort_on, reverse=True)
  
  return chars_arr
