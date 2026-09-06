import numpy as np


def get_vec():
    user_input = input("vector elements? ")
    elements = user_input.split()

    vector = []
    for x in elements:
        vector.append(float(x))

    return vector


def get_mat():
    rows = int(input("matrix rows count: "))

    matrix = []
    for i in range(rows):
        row_input = input(f"row {i+1}: ")
        row_elements = row_input.split()

        current_row = []
        for x in row_elements:
            current_row.append(float(x))

        matrix.append(current_row)

    return matrix

def dot_pro(A, v):
    mat = np.array(A)
    vec = np.array(v)
    return mat @ vec
