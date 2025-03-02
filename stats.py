# 
def count_words(text):
  """Counts words in text string

  Args:
      text (string): any text, will be split into array

  Returns:
      number: returns lenght of array (number of words)
  """
  words = text.split()
  return len(words)

def chars_dict(text):
  """Returns dictionary with symbols from text and number of their occurence

  Args:
      text (string): convert string to lower case (for no duplicit characters), each character will populate dictionary { "char": count }

  Returns:
      dictinary: ie. { "a": 5, ",": 34 }
  """
  chars_dict = {}
  text_lowered = text.lower()
  
  for char in text_lowered:
    if char in chars_dict:
      chars_dict[char] += 1
    else:
      chars_dict[char] = 1
  
  return chars_dict

def sort_by_value(single_value_dict):
  """Used for sorting of list containg single value dictionary. 

  Args:
      single_value_dict (dictionary): dictionary with single value {key: value}

  Returns:
      ?: value from dingle value dictionary 
  """
  return list(single_value_dict.values())[0]
  
def chars_dict_to_sorted_list(chars_dict):
  """Convert dictionary to list of dictionaries and sort by value

  Args:
      chars_dict (dictionary): dictionary of characters

  Returns:
      array: sorted array of dictionaries, sorted by dict. values
  """
  sorted_list = []

  for char in chars_dict:
    sorted_list.append({ char: chars_dict[char] })

  sorted_list.sort(key=sort_by_value, reverse=True)
  
  return sorted_list
