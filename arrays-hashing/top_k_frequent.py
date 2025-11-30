def topKFrequent(nums, k):
    # return: k most frequent
    most_freq_dict = {}

    # iterate through array and inc. value of element i in dict
    for i in range(len(nums)):
        if (nums[i] in most_freq_dict):
            most_freq_dict[nums[i]] += 1
        else:
            most_freq_dict[nums[i]] = 1

    # add most freq elemnt from dict to returned array and delete from dict k times
    most_freq_array = []
    i = 0
    while (i < k):
        maximum = max(most_freq_dict, key=most_freq_dict.get)
        most_freq_array.append(maximum)
        del most_freq_dict[maximum]
        i += 1
        
    return most_freq_array

nums=[1,2,2,3,3,3]
k=2
print(topKFrequent(nums, k))