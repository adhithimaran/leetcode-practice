def lengthOfLongestSubstring(s):
    if not s:
        return 0
    
    i = 0
    j = 0
    characters = set()
    max_length = 0
    
    while j < len(s):
        if s[j] not in characters:
            characters.add(s[j])
            j += 1
            max_length = max(max_length, j - i)
        else:
            characters.remove(s[i])
            i += 1
    
    return max_length


print(lengthOfLongestSubstring("zxyzxyz"))
print(lengthOfLongestSubstring("xxxx"))