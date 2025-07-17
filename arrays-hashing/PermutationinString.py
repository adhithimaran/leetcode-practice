def checkInclusion(s1, s2):
    s1 = sorted(s1)

    for i in range(len(s2)):
        for j in range(i, len(s2)):
            subStr = s2[i : j + 1]
            subStr = sorted(subStr)
            if subStr == s1:
                return True
    return False

s1="ab"
s2="lecabee"
print(checkInclusion(s1, s2))