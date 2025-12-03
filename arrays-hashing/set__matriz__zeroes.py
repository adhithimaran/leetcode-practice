"""
LeetCode #73: Set Matriz Zeroes
Difficulty: Medium
Topic: arrays

Problem:


Solution:

"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ref_matrix = [row[:] for row in matrix]
        for i in range(len(ref_matrix)):
            for j in range(len(ref_matrix[0])):
                if ref_matrix[i][j] == 0:
                    #row
                    for b in range(len(ref_matrix[0])):
                        matrix[i][b] = 0
                    #col
                    for a in range(len(ref_matrix)):
                        matrix[a][j] = 0


# Test cases
if __name__ == "__main__":
    sol = Solution()
    # Add test cases here
