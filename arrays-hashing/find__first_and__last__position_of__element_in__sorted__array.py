"""
LeetCode #34: Find First and Last Position of Element in Sorted Array
Difficulty: Medium
Topic: arrays

Problem:


Solution:

"""

class Solution(object):
    def solve(self, nums, target):
        """
        :rtype: 
        """
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            if target == nums[0]:
                return [0, 0]
            return [-1, -1]
        low = 0
        high = len(nums)-1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                upper = mid
                lower = mid

                while upper < len(nums) and nums[upper] == target:
                    upper+=1
                while lower >= 0 and nums[lower] == target:
                    lower-=1
                return [lower+1, upper-1]
            
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        if nums[low] == target:
            upper = low
            lower = low
            while upper < len(nums) and nums[upper] == target:
                upper += 1
            while lower >= 0 and nums[lower] == target:
                lower -= 1
            return [lower + 1, upper - 1]
        return [-1, -1]



# Test cases
if __name__ == "__main__":
    sol = Solution()
    # Add test cases here
    print(sol.solve([5,7,7,8,8,10], 8))
    print(sol.solve([5,7,7,8,8,10], 6))
    print(sol.solve([], 0))
    print(sol.solve([1], 1))
