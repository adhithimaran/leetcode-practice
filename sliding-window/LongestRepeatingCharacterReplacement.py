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
    for right in range(len(s)):
        print(f'current window:\n{s[left:right+1]}')
        replacements = k
        valid = True
        if (s[right] not in window_char_count):
            window_char_count[s[right]] = 1
        else:
            window_char_count[s[right]] += 1
        
        print(f'this is max key and value: {max(window_char_count.values())}')
        print(f'this is length of current window: {len(s[left:right+1])}')
        if (max(window_char_count.values()) + replacements) < len(s[left:right+1]):
            valid = False
            max_len = max(max_len, max(window_char_count.values()) + k)
            window_char_count[s[left]] -=1
            left +=1
    return max_len
        

s = "XYYX"
k = 2
print(characterReplacement(s, k))

s = "AAABABB"
k = 1
print(characterReplacement(s, k))