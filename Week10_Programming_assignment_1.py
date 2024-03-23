def rotate(mat):
    """
    Rotate a matrix 90 degrees clockwise.

    Argument:
    mat: list of lists
    Return:
    rotated_mat: list of lists
    """
    rotated_mat = []
    n_rows = len(mat)
    n_cols = len(mat[0])
    for j in range(n_cols):
        new_row = []
        for i in range(n_rows-1, -1, -1):
            new_row.append(mat[i][j])
        rotated_mat.append(new_row)

    return rotated_mat
