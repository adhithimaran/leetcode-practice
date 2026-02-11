def topKFrequent(nums, k):
    # k: int v: frequency
    # grab max and delete from map 
    # add to list and return 

    frquency_map = {}
    for i in range(len(nums)):
        curr = nums[i]
        if curr in frquency_map:
            frquency_map[curr] += 1
        else:
            frquency_map[curr] = 1
    
    most_freq = []
    j = 0
    while j < k:
        max_key = max(frquency_map, key=frquency_map.get)
        most_freq.append(max_key)
        del frquency_map[max_key]
        j+=1
    return most_freq

nums=[1,2,2,3,3,3]
k=2
print(topKFrequent(nums, k)) #Output: [2,3]