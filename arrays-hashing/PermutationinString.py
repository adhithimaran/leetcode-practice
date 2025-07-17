def checkInclusion(s1, s2):
    s1 = list(s1)
    s1.sort()
    s2 = list(s2)
    s2.sort()
    s1_string = ""
    s1_string.join(s1)
    s2_string = ""
    s2_string.join(s2)
    if s1 in s2:
        return True
    return False

s1="ab"
s2="lecabee"
print(checkInclusion(s1, s2))