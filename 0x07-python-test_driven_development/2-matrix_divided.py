#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix and returns the result without
    changing the original matrix.

    Args:
        matrix: a list of lists of integers or floats
        div: an integer or float to divide each element of the matrix by

    Returns:
        A new matrix with the same size as `matrix` containing the result
        of dividing each element of `matrix` by `div`.

    Raises:
        ZeroDivisionError: if `div` is zero
        TypeError: if `matrix` is not a matrix (list of lists) of
        integers or floats
                  if the rows of `matrix` have different sizes
                  if `div` is not an integer or float
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    size = len(matrix[0])
    div_matrix = []
    for row in matrix:
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        div_row = []

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)
            div_row.append(round(element / div, 2))
        div_matrix.append(div_row)
    return div_matrix
