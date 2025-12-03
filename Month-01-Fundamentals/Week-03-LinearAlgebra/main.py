import numpy as np

def matrix_multiply_scratch(A, B):

    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B :
        raise ValueError(f"Cannot multiply: A's columns ({cols_A}) != B's rows ({rows_B})")
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    print("Calculation Begins (From Scratch)...")

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def main():
    print("--- Matrix Multiplication: Scratch vs NumPy ---")

    matrix_A = [
        [1,5],
        [2,3],
        [1,7]
    ]

    matrix_B = [
        [1,2,3,7],
        [5,2,8,1]
    ]

    try:
        result_scratch = matrix_multiply_scratch(matrix_A, matrix_B)
        
        print("\n [Scratch] Result:")

        for row in result_scratch:
            print(row)

        np_A = np.array(matrix_A)
        np_B = np.array(matrix_B)

        result_numpy = np.dot(np_A, np_B)
        
        print("\n [NumPy] Result:")
        print(result_numpy)

        if np.allclose(result_scratch, result_numpy):
            print("\n SUCCESSFUL: Results match exactly!")
        else:
            print("\n ERROR: Results do not match.")
    
    except ValueError as e:
        print(f"\n ERROR: {e}")
    
if __name__ == "__main__":
    main()
