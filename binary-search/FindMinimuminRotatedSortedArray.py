def findMin(nums):
    if not nums:
        return -1
    r = len(nums)-1
    l = 0
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:  # Min is to the right
            l = m + 1
        else:  # Min is at mid or to the left
            r = m
    return nums[l]

nums1 = [3,4,5,6,1,2]
nums2 = [4,5,0,1,2,3]
nums3 = [4,5,6,7]

print(findMin(nums1))
print(findMin(nums2))
print(findMin(nums3))
