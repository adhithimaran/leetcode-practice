def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    
    """
    out = [[]]
    for num in range(len(nums)):
        # create the neew number (add or don't)
        number = nums[num]
        new_subsets = [] # to add to out
        for subset in range(len(out)):
            copy = out[subset][:] # copy of current subset
            copy.append(number) # add num to this one
            new_subsets.append(copy) 

        for k in range(len(new_subsets)):
            if (new_subsets[k] not in out):
                out.append(new_subsets[k])
    return out

print(subsets([1,2,3]))