def checkInclusion( s1, s2):
    print(f'this is s1: {s1}')
    print(f'this is s2: {s2}')
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    print(f'this is s1 sorted: {s1}')
    print(f'this is s2 sorted: {s2}')
    r = len(s1)-1
    for l in range(len(s2)):
        print(f'curr window: {s2[l:r+1]}')
        if (s2[l:r+1] == s1):
            return True
        if l == len(s2) - len(s1) + 1:
            return False
        r+=1
    return False

s1 = "xz"
s2 = "lecabeexzy"
print(checkInclusion(s1, s2))
