def debugging(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def rotate(matrix):
    n = len(matrix)
    for r in range(n//2):
        for c in range(r, n-r-1):

            temp = matrix[r][c]
            matrix[r][c] = matrix[n-1-c][r]
            matrix[n-1-c][r] = matrix[n-1-r][n-1-c]
            matrix[n-1-r][n-1-c] = matrix[c][n-1-r]
            matrix[c][n-1-r] = temp


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

debugging(matrix)
print(rotate(matrix))