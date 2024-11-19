"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
column are set to 0.
"""
def zeroMatrix(matrix: list[list[int]]) -> list[list[int]]:
    # Time Complexity: O(M * N)
    # Space Complexity: O(M + N)
    height = len(matrix)
    width = len(matrix[0])
    xList = []
    yList = []
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == 0:
                xList.append(x)
                yList.append(y)
    for y in set(yList):
        matrix[y] = [0] * width
    for x in set(xList):
        for i in range(height):
            matrix[i][x] = 0
    return matrix

def printMatrix(idx: int, matrix: list[list[int]]):
    print("rotateMatrix(matrix"+str(idx)+"): [")
    for idx, arr in enumerate(matrix):
        if idx != len(matrix) - 1:
            print('    ' + str(arr) + ',')
        else:
            print('    ' + str(arr))
    print("]")

matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]
printMatrix(1, zeroMatrix(matrix))

matrix = [
    [0, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
printMatrix(2, zeroMatrix(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
printMatrix(3, zeroMatrix(matrix))

matrix = [
    [1, 2, 3, 0],
    [4, 5, 6, 7],
    [7, 8, 9, 8]
]
printMatrix(4, zeroMatrix(matrix))

matrix = [
    [0, 0],
    [0, 0]
]
printMatrix(5, zeroMatrix(matrix))