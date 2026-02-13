
def productExceptSelf(nums):
    # compute product of list
    # loop through and divide product by curr
    product = 1
    for i in range(len(nums)):
        if nums[i] != 0:
            product *= nums[i]
    
    out_lst = []
    for i in range(len(nums)):
        if nums[i] == 0:
            out_lst.append(product)
        elif 0 in nums and nums[i] != 0:
            out_lst.append(0)
        else:
            out_lst.append(int(product/nums[i]))
    
    return out_lst


print(productExceptSelf([-1,0,1,2,3]))