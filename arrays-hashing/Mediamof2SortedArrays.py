def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # make one big list thats sorted
    # return the element at the middle index (odd and even length cases)

    merged_array = nums1 + nums2
    merged_array.sort()

    middle_idx = int(len(merged_array) / 2)
    if (len(merged_array) % 2 == 0):
        return (merged_array[middle_idx] + merged_array[middle_idx-1]) / 2.0
    else:
        m = len(merged_array) // 2
        return merged_array[m]
    
nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2)) # 2