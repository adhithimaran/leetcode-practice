def singleNumber( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if (len(nums) == 1):
        return nums[0]
    # array of ints (inputs) gets parsed to find the one integer that only appears once and returns as ouput
    # iterate through array
    nums.sort()
    i = 0
    j = 1
    while j < len(nums):
        if (nums[i] != nums[j]) :
            return nums[i]
        i+=2
        j+=2
    return nums[-1]
nums = [4,1,2,1,2]
print(singleNumber(nums))