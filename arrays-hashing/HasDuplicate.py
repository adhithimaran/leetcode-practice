class HasDuplicate:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] == nums[j]):
                    print(nums[i])
                    return True
        return False