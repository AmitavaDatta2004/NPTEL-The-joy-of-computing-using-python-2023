def is_magic(matrix):
  """
  This function checks if a square matrix is a magic square.

  Args:
      matrix: A square matrix represented as a list of lists of integers.

  Returns:
      "YES" if the matrix is a magic square, "NO" otherwise.
  """

  n = len(matrix)
  if not all(len(row) == n for row in matrix):
    return "NO"

  magic_constant = sum(matrix[0])

  for row in matrix:
    if sum(row) != magic_constant:
      return "NO"

  for col in zip(*matrix):
    if sum(col) != magic_constant:
      return "NO"

  diagonal_sum1 = sum(matrix[i][i] for i in range(n))
  diagonal_sum2 = sum(matrix[i][n - i - 1] for i in range(n))
  if diagonal_sum1 != magic_constant or diagonal_sum2 != magic_constant:
    return "NO"

  return "YES"
