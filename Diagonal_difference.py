# Calculate the difference between the diagonals of a matrix
# Time complexity - O(N^2)
# Space complexity - O(N)

def diagonalDifference(array):
    arrayLength = len(array) - 1
    sum1 = 0
    sum2 = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i == j:
                sum1 += array[i][j]
            if i + j == arrayLength:
                sum2 += array[i][j]
    return abs(sum1 - sum2)

array = [[1,2,3],[2,5,6],[9,8,9]]
diagonalDifference(array)
