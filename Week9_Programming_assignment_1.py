def balanced(word):
  """
  This function determines if a string containing parentheses is balanced.

  Args:
      word: A string containing parentheses.

  Returns:
      True if the string is balanced, False otherwise.
  """
  stack = []
  for char in word:
    if char in ("[", "{", "("):
      stack.append(char)
    elif char in ("]", "}", ")"):
      if not stack:
        return False
      top = stack.pop()
      if not matches(top, char):
        return False
  return not stack

def matches(opening, closing):
  """
  This function determines if an opening parenthesis matches a closing parenthesis

  Args:
      opening: The opening parenthesis

      closing: The closing parenthesis

  Returns:
      True if the parentheses match, False otherwise
  """
  return (opening == "(" and closing == ")") or (opening == "{" and closing == "}") or (opening == "[" and closing == "]")
