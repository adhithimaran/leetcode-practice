def isPalindrome(s):
    # unify cases 
    lower_s = s.lower()
    # remove spaces
    no_space_s = lower_s.replace(" ", "")
    
    # remove other non-alphanumeric characters
    i = 0
    while i < len(no_space_s):
        lower_a = ord("a")
        lower_z = ord("z")
        upper_a = ord("A")
        upper_z = ord("Z")
        zero = ord("0")
        nine = ord ("9")
        curr = ord(no_space_s[i])
        if ((lower_a <= curr <= lower_z) or (upper_a <= curr <= upper_z) or (zero <= curr <= nine)) == False:
            no_space_s = no_space_s[:i] + no_space_s[i+1:]
        i +=1
    # check og against reversed [::-1]
    reversed_s = no_space_s[::-1]
    if reversed_s == no_space_s:
        return True
    return False

print(isPalindrome("Was it a car or a cat I saw?"))
print(isPalindrome("tab a cat"))