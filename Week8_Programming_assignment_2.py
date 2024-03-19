def minor_matrix(M, i, j):
  """
  This function calculates the minor matrix of a square matrix M 
  by removing the i-th row and j-th column.

  Args:
      M: A square matrix represented as a list of lists.
      i: A non-negative integer representing the row index.
      j: A non-negative integer representing the column index.

  Returns:
      A new matrix (list of lists) representing the minor matrix of M.
  """
  M_ij = []
  for row_index, row in enumerate(M):
    if row_index != i:
      new_row = []
      for col_index, value in enumerate(row):
        if col_index != j:
          new_row.append(value)
      M_ij.append(new_row)
  return M_ij
