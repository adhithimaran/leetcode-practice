s = "Was it a car or a cat I saw?"


# What is a valid character? A-Z, a-z, 0-9
# Case 1: valid I, invalid J
# Case 2: invalid I, valid J
# Case 3: both I + J are invalid
# Case 4: both I + J are valid

def isPalindrome(s):
   s = s.lower()
   j = len(s)-1
   i = 0
   while i < len(s):
       print(f'does {s[i]} == {s[j]}')
       # What is a valid character? A-Z, a-z, 0-9
       i_valid = False
       j_valid = False
       if ("A" <= s[i] <= "Z") or ("a" <= s[i] <= "z") or ("0" <= s[i] <= "9"):
           i_valid = True
       if ("A" <= s[j] <= "Z") or ("a" <= s[j] <= "z") or ("0" <= s[j] <= "9"):
           j_valid = True

       # Case 1: valid I, invalid J
           # i stays, j moves
       if (i_valid == True and j_valid == False):
           j-=1
           continue
       # Case 2: invalid I, valid J
           # i moves, j stays
       elif (i_valid == False and j_valid == True):
           i += 1
           continue
       # Case 3: both I + J are invalid
       elif (i_valid == False and j_valid == False):
           j-=1
           i += 1
           continue
       # Case 4: both I + J are valid (must check here)
       else:
           if (s[i] != s[j]):
               return False
           j-=1
           i += 1
   return True

print(isPalindrome(s))

