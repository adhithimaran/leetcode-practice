def search(nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r: 
            mid = l + ((r-l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid -1
        return -1

# Input: 
nums = [-1,0,2,4,6,8]
target = 4
# Output: 3
print(search(nums, target))