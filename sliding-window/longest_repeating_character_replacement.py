def characterReplacement(s, k):
    # input: 
        # string with only capital letters
        # integer: how many letters I can replace 
    # output:
        # len: longest substring of repeating characters
    
    # Case 1: added character is same
        # Case 2: character not same but have k integer
        # Case 3: character is not same , no more k int
    max_len = 0
    left = 0
    window_char_count = {}
    max_char_count = 0
    for right in range(len(s)):
        if (s[right] not in window_char_count):
            window_char_count[s[right]] = 1
        else:
            window_char_count[s[right]] += 1
        max_char_count = max(max_char_count, window_char_count[s[right]])
        window_size = right-left+1
        if window_size - max_char_count > k:
            window_char_count[s[left]] -=1
            left+=1
        max_len = max(max_len, right-left+1)
    return max_len
        

s="AAAA"
k = 2
print(characterReplacement(s, k))

s = "AAABABB"
k = 1
print(characterReplacement(s, k))