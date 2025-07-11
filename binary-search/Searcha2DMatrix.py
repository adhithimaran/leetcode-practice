def searchMatrix(matrix, target):
    print(f'this is matrix:\n {matrix}')
    if not matrix:
        return -1
    if target > matrix[-1] or target < matrix[0]:
        return -1
    
    rows = len(matrix)
    curr_row = 0
    while curr_row < rows:
        high = len(matrix[curr_row])-1
        low = 0
        while (high >= low):
            mid = (low + high) // 2
            if (target < matrix[curr_row][mid]):
                high = mid-1
            elif (target > matrix[curr_row][mid]):
                low = mid+1
            else:
                return mid
        curr_row+=1
    return -1


matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10 #(true)

print(searchMatrix(matrix, target))