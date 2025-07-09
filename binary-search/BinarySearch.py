# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

def search(nums, target):
    if not nums:
        return -1
    if target > nums[-1] or target < nums[0]:
        return -1
    high = len(nums)-1
    low = 0
    while (high >= low):
        mid = (low + high) // 2
        if (target < nums[mid]):
            high = mid-1
        elif (target > nums[mid]):
            low = mid+1
        else:
            return mid
    return -1

nums = [-1,0,2,4,6,8]
target = 4
print(search(nums, target))

# nums = [-1,0,2,4,6,8]
# target = 3
# print(search(nums, target))
