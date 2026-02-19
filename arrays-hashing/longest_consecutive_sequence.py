def longestConsecutive(nums):
    # sort
    nums_sorted = sorted(nums)
    # skip over duplicates while counting
    max_count = 0
    temp_count = 1
    i = 0
    j = 1
    while j < len(nums_sorted):
        i = j-1
        curr_ele = nums_sorted[i]
        next_ele = nums_sorted[j]
        if curr_ele == next_ele:
            del nums_sorted[j]
        elif (curr_ele + 1) != next_ele:
            max_count = max(max_count, temp_count)
            temp_count = 1
            j +=1
            # del nums_sorted[j]
        else: 
            temp_count +=1
            max_count = max(max_count, temp_count)
            j +=1
    return max_count

nums = [9,1,4,7,3,-1,0,5,8,-1,6] #7
nums1 = [0,3,2,5,4,6,1,1] # 7 

print(longestConsecutive(nums))
print(longestConsecutive(nums1))