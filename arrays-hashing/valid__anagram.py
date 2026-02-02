"""
LeetCode #242: Valid Anagram
Difficulty: Easy
Topic: Arrays

Problem:


Solution:

"""

class Solution(object):
    def solve(self, s: str, t: str) -> bool:
        s_alpa = sorted(s)
        t_alpha = sorted(t)
        if s_alpa == t_alpha:
            return True
        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    # Add test cases here
