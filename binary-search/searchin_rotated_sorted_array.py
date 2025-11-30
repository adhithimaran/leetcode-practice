def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = (l + r) // 2
        
        # Check if we found the target
        if nums[m] == target:
            return m
        
        # Determine which half is sorted
        if nums[l] <= nums[m]:  # Left half is sorted
            # Check if target is in the sorted left half
            if nums[l] <= target < nums[m]:
                r = m - 1  # Search left half
            else:
                l = m + 1  # Search right half
        else:  # Right half is sorted
            # Check if target is in the sorted right half
            if nums[m] < target <= nums[r]:
                l = m + 1  # Search right half
            else:
                r = m - 1  # Search left half

    
    return -1

nums=[3,5,1]
target=3
print(search(nums, target))
