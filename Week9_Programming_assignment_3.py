def power(A, m):
  """
  This function computes the power of a square matrix A raised to a positive integer m using recursion.

  Args:
      A: A square matrix.
      m: A positive integer representing the power.

  Returns:
      A raised to the power m.
  """
  if m == 0:
    return [[1 if i == j else 0 for j in range(len(A))] for i in range(len(A))]
  elif m == 1:
    return A
  else:
    return matrix_multiply(power(A, m-1), A)

def matrix_multiply(A, B):
  """
  This function multiplies two matrices A and B.

  Args:
      A: The first matrix.
      B: The second matrix.

  Returns:
      The product of A and B.
  """
  result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]
  return result
