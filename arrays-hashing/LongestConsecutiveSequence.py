def longestConsecutive(self, nums: List[int]) -> int:
    if nums == []:
        return 0
    nums.sort()
    curr_len = 1
    lengths = []
    for i in range(len(nums)-1):
        if (nums[i] + 1 == nums[i+1]):
            curr_len +=1
        else:
            if (nums[i] != nums[i+1]):
                lengths.append(curr_len)
                curr_len = 1
    lengths.append(curr_len)
    return max(lengths)