def characterReplacement(s, k):
    # input: 
        # string with only capital letters
        # integer: how many letters I can replace 
    # output:
        # len: longest substring of repeating characters
    max_length = 0
    left = 0
    for right in range(len(s)):
        window_char_count = {}
        replacements = k
        valid = True
        while valid:
            if (s[right] not in window_char_count):
                window_char_count[s[right]] = 1
            else:
                window_char_count[s[right]] += 1
            # Case 1: added character is same
            # Case 2: character not same but have k integer
            # Case 3: character is not same , no more k int

s = "XYYX"
k = 2
print(characterReplacement(s, k))

s = "AAABABB"
k = 1
print(characterReplacement(s, k))