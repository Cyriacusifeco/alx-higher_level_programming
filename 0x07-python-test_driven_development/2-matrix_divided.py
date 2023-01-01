#!/usr/bin/python3
"""
This is a module that divides all the elements of a matrix and returns the
result without changing the original matrix.

"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix

    """

    j = 0
    i = 0

    size = len(matrix[0])

    div_matrix = matrix

    if div == 0:
        raise ZeroDivisionError("division by zero")

    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    else:
        for i, row in enumerate(matrix):
            if size != len(row):
                raise TypeError(
                    "Each row of the matrix must have the same size"
                    )

            else:
                for j, element in enumerate(row):
                    if not isinstance(element, int) and not


isinstance(element, float):
                        raise TypeError(
                        "matrix must be a matrix (list of lists)
of integers/floats"

                        )

                    else:
                        div_matrix = [[round(element / div, 2) for 
element in row] for row in matrix]

    return (div_matrix)
