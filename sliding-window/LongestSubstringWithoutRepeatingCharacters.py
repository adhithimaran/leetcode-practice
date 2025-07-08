def lengthOfLongestSubstring(s):
    print(f'this is s: \n {s}')
    i = 0
    j = 0
    characters = []
    lengths = 0

    while i < len(s):
        print(f'this is i: {s[i]}')
        print(f'this is i: {s[j]}')
        print(f'this is substring: {s[i:j+1]}')
        if (s[j] in characters):
            lengths = max(lengths, len(s[i:j]))
            i+=1
            j = i
            continue
        characters.append(s[j])
        print(characters)
        j+=1
    return lengths


print(lengthOfLongestSubstring("zxyzxyz"))
print(lengthOfLongestSubstring("xxxx"))