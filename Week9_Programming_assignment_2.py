def depth(expr):
  """
  This function calculates the maximum nesting depth in a balanced expression.

  Args:
      expr: A balanced expression string containing only flower brackets "()".

  Returns:
      The maximum nesting depth in the expression.
  """
  max_depth = 0
  current_depth = 0
  for ch in expr:
    if ch == '(':
      current_depth += 1
      max_depth = max(max_depth, current_depth)
    elif ch == ')':
      if current_depth == 0:
        return -1
      current_depth -= 1
  return max_depth if current_depth == 0 else -1
