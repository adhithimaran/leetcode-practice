"""
LeetCode #290: Word Pattern
Difficulty: Easy
Topic: hash

Problem:


Solution:

"""

class Solution(object):
    def solve(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if len(pattern) != len(s):
            return False

        s_lst = s.split(" ")
        print(s_lst)
        map = {} # tuples
        for i in range(len(pattern)):
            word = s_lst[i]
            letter = pattern[i]
            # Invalid: new word, letter in dict
            if (word not in map.values()) and (letter in map):
                return False
            # Maybe Valid: seen word, letter in dict
            if (word in map.values()) and (letter in map) and (map[letter] != word):
                return False
            # Invalid: seen word, letter not in dict
            if (word in map.values()) and (letter not in map):
                return False
            # Valid: new word, letter not in dict
            if (word not in map.values()) and (letter not in map):
                map[letter] = word
        return True
            


# Test cases
if __name__ == "__main__":
    sol = Solution()
    # Add test cases here
    pattern = "abba"
    s = "dog cat cat dog"
    sol.solve(pattern, s)
