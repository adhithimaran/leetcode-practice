def maxArea(heights):
    l = 0
    r = len(heights)-1
    max_area = -1
    while l<r:
        left_h = heights[l]
        right_h = heights[r]
        width = r-l
        height = min(left_h, right_h)
        curr_area = width * height
        max_area = max(curr_area, max_area)
        if left_h > right_h:
            r-=1
        else:
            l+=1
    return max_area


height = [1,7,2,5,4,7,3,6] # 36
height_1 = [2,2,2] # 4
print(maxArea(height))
print(maxArea(height_1))