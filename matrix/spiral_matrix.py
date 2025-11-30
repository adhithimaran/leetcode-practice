
def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    row_length = len(matrix)
    col_length = len(matrix[0])
    spiral_output = []
    while matrix:
        top = matrix.pop(0)
        spiral_output.append(top)
        bottom = matrix.pop(-1)
        bottom.reverse()
        spiral_output.append(bottom)
        
        row_length = len(matrix)
        col_length = len(matrix[0])
        while 

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))