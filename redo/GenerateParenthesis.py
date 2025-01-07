from itertools import permutations
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        string = ''
        while n > 0:
            string += ()
            n-=1
        list = []
        for permutation in permutations(string):
            list.append(permutation)
        return list
if __name__ == '__main__':
    solution = Solution()  # Create an instance of the Solution class
    result = solution.generateParenthesis(1)  # Call the method with n = 1
    print(result)