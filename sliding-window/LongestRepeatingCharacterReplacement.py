def characterReplacement(s, k):
    # input: 
        # string with only capital letters
        # integer: how many letters I can replace 
    # output:
        # len: longest substring of repeating characters
    max_length = 0
    left = 0
    for right in range(len(s)):
        uniques = k
        # Case 1: added character is same
        # Case 2: character not same but have k integer
        # Case 3: character is not same , no more k int

s = "XYYX"
k = 2
print(characterReplacement(s, k))

s = "AAABABB"
k = 1
print(characterReplacement(s, k))