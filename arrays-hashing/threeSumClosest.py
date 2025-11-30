def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Simplify:
            in: int array nums, int target
            out: sum of 3 ints in nums that's closest to target
        Pattern Rec:
            - find all combinations of groups of 3
        Implementation:
            - closest sum
            - case 1: n == 3 -> return the sum of the current list
            - case 2: n > 3 -> find all combos (3 for loops)
                - check sum of 3 against closest_sum variable (use abs func)
            return closest sum
        Coding:
        Debug:
        """
        if (len(nums) == 3): # n == 4
            return nums[0] + nums[1] + nums[2]

        closest_sum = -1001 # setting to unreachable number
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    curr_sum = nums[i] + nums[j] + nums[k]
                    diff = abs(target - curr_sum)
                    if (diff < abs(target - closest_sum)):
                        closest_sum = curr_sum
        return closest_sum