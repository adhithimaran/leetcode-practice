def isValid(s):
    if (len(s) % 2 != 0):
        return False 
    half = int(len(s)/2)
    list1 = list(s[:half])
    list2 = list(s[half:])
    list2.reverse()
    print(list1)
    print(list2)
    for i in range(len(list1)):
        if (list1[i] == '{' and list2[i] != '}'):
            return False
        elif (list1[i] == '[' and list2[i] != ']'):
            return False
        elif (list1[i] == '(' and list2[i] != ')'):
            return False
    return True
s = "([{}])"
print(isValid(s))

