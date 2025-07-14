def search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (r+l) // 2
        print(f'low: {nums[l]}\nhigh: {nums[r]}\nmid: {nums[m]}\n')
        if (nums[m] > nums[r] and nums[m] > target):
            l = m+1
        elif (nums[m] < nums[r] and nums[m] < target):
            r = m-1
        elif (nums[m] < nums[r] and nums[m] > target):
            l = m+1
        elif (nums[m] > nums[r] and nums[m] < target):
            r = m-1
        
        
    return -1

nums = [3,4,5,6,1,2]
target = 1
#print(search(nums, target))

nums = [3,5,6,0,1,2]
target = 4
print(search(nums, target))
