def lengthOfLongestSubstring(s):
    i = 0
    j = 0
    characters = []
    lengths = 0

    while j < len(s):
        if (s[j] in characters):
            lengths = max(lengths, len(s[i:j]))
            i+=1
            j = i
            continue
        characters.append(s[j])
        j+=1
    return lengths


print(lengthOfLongestSubstring("zxyzxyz"))
print(lengthOfLongestSubstring("xxxx"))