def twoSum(nums, target):
    i, j = 0, 1
    while i < len(nums)-1:
        ith = nums[i]
        jth = nums[j]
        if ith + jth == target:
            return [i, j]

        if j != len(nums)-1:
            j += 1
        else:
            i += 1
            j = i+1


nums = [5,5]
target = 10

print(twoSum(nums, target))