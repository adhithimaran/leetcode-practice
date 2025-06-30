def twoSum(numbers, target):
    # loop through array (2 ptrs)
    left = 0
    right = len(numbers)-1
    while left != len(numbers)-1 or right != 0:
        print(f'i = {numbers[left]}')
        print(f'j = {numbers[right]}')
        int_sum = numbers[left] + numbers[right]
        if (int_sum == target):
            return [numbers[left], numbers[right]]
        elif (int_sum > target):
            right -=1
        else:
            left +=1


numbers=[2,3,4]
target=6
print(twoSum(numbers, target))