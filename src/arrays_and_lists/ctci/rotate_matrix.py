from typing import List

from utils.utils import pretty_print_matrix

# For this problem, first we can utilize a dictionary to store the values that we have moved
# As we move the values around. However this will require O(n) space
# Can we do this in place? If we attempt to move this in place step by step, we can see that
# We can treat the matrix as a set of layers. We can rotate each layer one by one
# How do we find the number of layers? when n is 4, we have 2 layers, when n is 5, we have 2 layers
# When n is 6, we have 3 layers, when n is 7, we have 3 layers, when n is 8, we have 4 layers
# We now notice the trend that the number of layers is n // 2
# Then we have to find the first and last index of each layer
# The first index of the layer of an nxn matrix is from 0 to n//2
# The last index of the layer of an nxn matrix is from n - 1 - layer

def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    print("before")
    pretty_print_matrix(matrix)
    # First we find the length n of the matrix
    n = len(matrix)
    # If we pretend the matrix is a set of layers, we can rotate each layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        # At each iteration, we rotate 4 elements of a layer from the start to the last index of the layer
        # Offset here is pretty much the distance from the first index of the layer to the current element
        # We use this to keep track of which element we are moving
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top

    print("after")
    pretty_print_matrix(matrix)
    


if __name__ == '__main__':
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # rotate_matrix(matrix)
    # print(matrix)
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate_matrix(matrix)
    # matrix = [[1, 2], [3, 4]]
    # rotate_matrix(matrix)
    # print(matrix)
    # matrix = [[1]]
    # rotate_matrix(matrix)
    # print(matrix)
    # matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    # rotate_matrix(matrix)
    # print(matrix)
