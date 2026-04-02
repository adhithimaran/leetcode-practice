def lengthOfLongestSubstring(s):
        # Edge Case(s): s.len <= 1
        if (len(s) <= 1):
            return len(s)
        # Normal Case: s.length > 1
        # 1. check is char exists in DS
            # a. exists -> loop (change window and check again until no dupes)
            # b. doesn't exist -> add char to DS and window
        # 2. add to DS

        substring = ""
        longest = 0
        for i in range(len(s)):
            curr = s[i]
            while curr in substring:
                substring = substring[1:]
            substring += curr
            longest = max(longest, len(substring))
        return longest

print(lengthOfLongestSubstring("cdd"))   # 2
print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("pwwkew"))    # 3