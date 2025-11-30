def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    nums.sort()
    while val in nums:
        index = nums.index(val)
        nums.pop(index)
    return len(nums)
nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))