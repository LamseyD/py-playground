from typing import List

from src.utils.utils import pretty_print_matrix
def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    print("before")
    pretty_print_matrix(matrix)
    n = len(matrix)
    m = len(matrix[0])
    seen = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                seen.append([i,j])

    for i in range(len(seen)):
        for j in range(m):
            matrix[seen[i][0]][j] = 0

        for j in range(n):
            matrix[j][seen[i][1]] = 0
            
    print("after")
    pretty_print_matrix(matrix)

def zero_matrix_copilot(matrix: List[List[int]]) -> List[List[int]]:
    print("before")
    pretty_print_matrix(matrix)
    n = len(matrix)
    m = len(matrix[0])
    row_has_zero = False
    col_has_zero = False

    # First we determine if the first row and first column has a zero
    for i in range(m):
        if matrix[0][i] == 0:
            row_has_zero = True
            break

    for i in range(n):
        if matrix[i][0] == 0:
            col_has_zero = True
            break

    # This approach is similar to the one above, 
    # but we use the first row and first column to store the zeros 
    # to find out which column and rows we need to turn 0
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, n):
        if matrix[i][0] == 0:
            for j in range(1, m):
                matrix[i][j] = 0

    for i in range(1, m):
        if matrix[0][i] == 0:
            for j in range(1, n):
                matrix[j][i] = 0

    if row_has_zero:
        for i in range(m):
            matrix[0][i] = 0

    if col_has_zero:
        for i in range(n):
            matrix[i][0] = 0

    print("after")
    pretty_print_matrix(matrix)

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 0, 8], [0, 10, 11, 12]]
    zero_matrix(matrix)
    print("=====================================")
    matrix = [[1, 2, 3, 4], [5, 6, 0, 8], [0, 10, 11, 12]]
    zero_matrix_copilot(matrix)