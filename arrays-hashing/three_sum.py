def threeSum(nums):
    # given: int [] nums
    # return: all triplets [i, j, k] (indexes), where (i + j + k == 0) AND (i, j and k are distinct)

    # norm case: len > 3
    # edge case: len == 3
    combinations = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                combo = [nums[i], nums[j], nums[k]]
                combo.sort()
                if (nums[i] + nums[j] + nums[k] == 0) and (i != j != k) and (combo not in combinations):
                    combinations.append(combo)
    return combinations

print(threeSum([-1,0,1,2,-1,-4]))
    