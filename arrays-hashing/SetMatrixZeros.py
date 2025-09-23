def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # iterate through whole matrix
    # if element == 0
        # iterate through row and col again and set to 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                #row
                for b in range(len(matrix[0])):
                    matrix[i][b] = 0
                #col
                for a in range(len(matrix)):
                    matrix[a][i] = 0

matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]]
print(setZeroes(matrix))