import numpy as np
from functions import *

def main():
    vector = get_vec()
    matrix_data = get_mat()
    matrix_np = np.array(matrix_data)
    prod = dot_pro(matrix_data, vector)

    print("A = ")
    print(matrix_np)
    print("v = ", vector)
    print("Av = ", prod)

if __name__ == "__main__":
    main()

