import numpy as np
from functions import get_vec, get_mat

def main():
    vector = get_vec()
    
    matrix_data = get_mat()
    matrix_np = np.array(matrix_data)
    print("your vector = ", vector)
    print("your matrix:")
    print(matrix_np)

if __name__ == "__main__":
    main()