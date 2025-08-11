def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # input: array of nums
    # if you can jump to end at a position true, else false
    # output: boolean True or False
    if len(nums) == 1:
        return True

    farthest = 0
    for i in range(len(nums)-1):
        if i > farthest:
            return False
        farthest = max(nums[i] + i, farthest)
        if farthest >= len(nums) - 1: # 1 + 2
            return True
    return False