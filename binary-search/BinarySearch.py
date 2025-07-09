# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

def search(nums, target):
    high = len(nums)-1
    low = 0
    while (high >= low):
        mid = (high - low) // 2
        print(f'this is high: {nums[high]}')
        print(f'this is low: {nums[low]}')
        print(f'this is mid: {nums[mid]}')
        print(f'current windoe: {nums[low:high+1]}')
        if (target < nums[mid]):
            high = mid
        elif (target > nums[mid]):
            low = mid
        else:
            return mid

nums = [-1,0,2,4,6,8]
target = 4
print(search(nums, target))
