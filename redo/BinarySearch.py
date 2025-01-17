def search( nums, target):
    left = 0
    right = len(nums) -1
    while (left <= right):
        mid = (right + left) //2
        if nums[mid] == target:
            return mid            
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1

# Input: 
nums = [-1,0,2,4,6,8]
target = 4
# Output: 3
print(search(nums, target))