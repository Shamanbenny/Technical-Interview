"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 
bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 
"""
def rotateMatrix(matrix: list[list[int]]) -> list[list[int]]:
    if len(matrix) == 1:
        return matrix
    for layer in range((len(matrix) + 1) // 2):
        first = layer
        last = len(matrix) - 1 - layer
        for idx in range(first, last):
            tmp = matrix[first][idx]
            matrix[first][idx] = matrix[-idx-1][first]
            matrix[-idx-1][first] = matrix[last][-idx-1]
            matrix[last][-idx-1] = matrix[idx][last]
            matrix[idx][last] = tmp
    return matrix
# Extremely difficult to understand...
# But basically, we're rotating the matrix in layers like an onion.
"""
Given a 5 by 5 matrix...
We rotate all * and ignore O...

First Loop:         Second Loop:        Third Loop:
* * * * *           O O O O O           O O O O O
* O O O *           O * * * O           O O O O O
* O O O *           O * O * O           O O * O O
* O O O *           O * * * O           O O O O O
* * * * *           O O O O O           O O O O O
"""

def printMatrix(idx: int, matrix: list[list[int]]):
    print("rotateMatrix(matrix"+str(idx)+"): [")
    for idx, arr in enumerate(matrix):
        if idx != len(matrix) - 1:
            print('    ' + str(arr) + ',')
        else:
            print('    ' + str(arr))
    print("]")

matrix4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
printMatrix(4, rotateMatrix(matrix4))


matrix3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
printMatrix(3, rotateMatrix(matrix3))

matrix2 = [
    [1, 2],
    [3, 4]
]
printMatrix(2, rotateMatrix(matrix2))

matrix1 = [
    [1]
]
printMatrix(1, rotateMatrix(matrix1))