def hasDuplicate(self, nums: List[int]) -> bool:
       # BF: iterate through nums n times and check if element appears twice, return true
       # O(n squared)
       nums.sort()
       for i in range(len(nums)-1):
            curr = nums[i]
            next_ele = nums[i+1]
            if (curr == next_ele):
                return True
       return False