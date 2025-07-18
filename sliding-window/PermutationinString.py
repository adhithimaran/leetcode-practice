def checkInclusion(s1, s2):
    print(f'this is s1: {s1}')
    print(f'this is s2: {s2}')
    
    # Handle edge cases
    if len(s1) > len(s2):
        return False
    
    s1_sorted = sorted(s1)
    print(f'this is s1 sorted: {s1_sorted}')
    
    # Check each window of size len(s1) in s2
    for l in range(len(s2) - len(s1) + 1):
        window = s2[l:l + len(s1)]
        window_sorted = sorted(window)
        print(f'curr window: {window} -> sorted: {window_sorted}')
        
        if window_sorted == s1_sorted:
            return True
    
    return False

# Test cases
print("Test 1:", checkInclusion("ab", "eidbaooo"))  # Should return True
print("\nTest 2:", checkInclusion("ab", "eidboaoo"))  # Should return False
print("\nTest 3:", checkInclusion("abc", "bac"))      # Should return True
