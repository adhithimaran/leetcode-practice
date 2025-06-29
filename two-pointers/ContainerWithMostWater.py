def maxArea(heights):
    j = len(heights) - 1
    max_sum = 0
    for i in range(len(heights)):
        temp_sum = 0
        for k in range(i, j):
            temp_sum += heights[k]
            print(f'this is the end points: {heights[i]} and {heights[k]}')
            print(f'sum: {temp_sum}')
            if temp_sum > max_sum:
                max_sum = temp_sum
        j-=1

height = [1,7,2,5,4,7,3,6]
print(maxArea(height))