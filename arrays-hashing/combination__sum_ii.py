"""
LeetCode #40: Combination Sum II
Difficulty: Medium
Topic: arrays

Problem:


Solution:

"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Important!
        results = []
        def backtrack(start_index, current_combination, remaining_target):
            if remaining_target == 0:
                results.append(current_combination[:])  # Why [:] ?
                return
            
            if remaining_target < 0:
                return
            
            for i in range(start_index, len(candidates)):
                if (i > start_index) and (candidates[i] == candidates[i-1]):
                    continue
                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, remaining_target - candidates[i])
                current_combination.pop()
        
        backtrack(0, [], target)
        return results



# Test cases
if __name__ == "__main__":
    sol = Solution()
    # Add test cases here
