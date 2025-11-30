def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i+1 < len(nums):
        print(f'nums[i]: {nums[i]}')
        if nums[i] == nums[i+1]:
            print(f'{nums[i]} == {nums[i+1]}')
            j = i +1
            while (j < len(nums) and nums[j] == nums[i]):
                print(f'{nums[i]} == {nums[j]}')
                nums.pop(j)
                
        i +=1
    return len(nums)

nums =[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))