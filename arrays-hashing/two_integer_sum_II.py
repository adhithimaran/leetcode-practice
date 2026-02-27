def twoSum(numbers, target):
    sorted_nums = sorted(numbers)
    i = 0 
    j = 1
    while i < len(sorted_nums):
        if sorted_nums[i] + sorted_nums[j] == target:
            og_list_i = numbers.index(sorted_nums[i])
            og_list_j = numbers.index(sorted_nums[j])
            return [og_list_i+1, og_list_j+1]
        if (j == len(sorted_nums) -1):
            i += 1
            j = i+ 1
        else:
            j += 1

# print(twoSum([100,200,300,500], 500)) # [1,2]

numbers=[-50,-48,-46,-44,-42,-40,-38,-36,-34,-32,-30,-28,-26,-24,-22,-20,-18,-16,-14,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
target=-96
print(twoSum(numbers, target))