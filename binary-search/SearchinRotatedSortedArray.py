def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = (l + r) // 2
        
        # Check if we found the target
        if nums[m] == target:
            return m 
        
        if nums[m] > target:
            if nums[m] > nums[r]:
                # right
                l = m+1
            else:
                # left
                r = m-1
        
        else:
            if nums[m] > nums[r]:
                # left
                r = m-1
            else:
                #right
                l = m+1

    
    return -1

nums=[3,5,1]
target=3
