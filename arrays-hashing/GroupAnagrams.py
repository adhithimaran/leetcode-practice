def sol(strs):
    anagram_group_list = []
    if (len(strs) <= 1) :
        return [strs]
    # iterate through strs (if length is greater than 1)
        # sort each element and check against each group made in out list
        # add to that group or make a new group
    # return out list
    for i in range(len(strs)):
        if (i == 0): 
            anagram_group_list.append([strs[i]])
            continue
                
        sorted_ele = sorted(strs[i])
        added = False
        for j in range(len(anagram_group_list)):
            if (sorted_ele == sorted(anagram_group_list[j][0])):
                anagram_group_list[j].append(strs[i])
                added = True
                break

        if (added != True):
            anagram_group_list.append([strs[i]])

    return anagram_group_list

strs=["act","pots","tops","cat","stop","hat"]

print(sol(strs))