# Time: O(n)
# Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # loop through array (2 ptrs)
        left = 0
        right = len(numbers)-1
        while left < right:
            int_sum = numbers[left] + numbers[right]
            if (int_sum == target):
                return [left+1, right+1]
            elif (int_sum > target):
                right -=1
            else:
                left +=1


numbers=[2,3,4]
target=6
print(twoSum(numbers, target))