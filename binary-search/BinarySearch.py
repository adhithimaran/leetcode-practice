# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

def search(nums, target):
    if not nums:
        return -1
    if target > nums[-1] or target < nums[0]:
        return -1
    high = len(nums)-1
    low = 0
    while (high >= low):
        mid = (low + high) // 2
        if (target < nums[mid]):
            high = mid-1
        elif (target > nums[mid]):
            low = mid+1
        else:
            return mid
    return -1

# nums = [-1,0,2,4,6,8]
# target = 4
# print(search(nums, target))

# nums = [-1,0,2,4,6,8]
# target = 3
# print(search(nums, target))

def run_tests():
    test_cases = [
        # Basic cases
        ([-1, 0, 2, 4, 6, 8], 4, 3),  # Original example
        ([-1, 0, 2, 4, 6, 8], 0, 1),  # Found at index 1
        ([-1, 0, 2, 4, 6, 8], 8, 5),  # Found at last index
        ([-1, 0, 2, 4, 6, 8], -1, 0), # Found at first index
        
        # Not found cases
        ([-1, 0, 2, 4, 6, 8], 3, -1),  # Between existing elements
        ([-1, 0, 2, 4, 6, 8], -2, -1), # Less than minimum
        ([-1, 0, 2, 4, 6, 8], 10, -1), # Greater than maximum
        
        # Edge cases
        ([], 1, -1),           # Empty array
        ([5], 5, 0),           # Single element - found
        ([5], 3, -1),          # Single element - not found
        ([1, 2], 1, 0),        # Two elements - first
        ([1, 2], 2, 1),        # Two elements - second
        ([1, 2], 3, -1),       # Two elements - not found
        
        # Odd length arrays
        ([1, 3, 5, 7, 9], 1, 0),       # First element
        ([1, 3, 5, 7, 9], 5, 2),       # Middle element
        ([1, 3, 5, 7, 9], 9, 4),       # Last element
        ([1, 3, 5, 7, 9], 6, -1),      # Not found
        
        # Even length arrays
        ([2, 4, 6, 8, 10, 12], 2, 0),   # First element
        ([2, 4, 6, 8, 10, 12], 8, 3),   # Middle-ish element
        ([2, 4, 6, 8, 10, 12], 12, 5),  # Last element
        ([2, 4, 6, 8, 10, 12], 5, -1),  # Not found
        
        # Negative numbers
        ([-10, -5, -2, 0, 3, 7], -5, 1),   # Negative found
        ([-10, -5, -2, 0, 3, 7], -1, -1),  # Negative not found
        ([-10, -5, -2, 0, 3, 7], 0, 3),    # Zero found
        
        # All negative numbers
        ([-8, -6, -4, -2, -1], -4, 2),     # Found
        ([-8, -6, -4, -2, -1], -3, -1),    # Not found
        
        # Large numbers
        ([100, 200, 300, 400, 500], 300, 2),   # Found
        ([100, 200, 300, 400, 500], 250, -1),  # Not found
        
        # Consecutive numbers
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 0),   # First
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 9),  # Last
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 4),   # Middle
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, -1), # Not found
        
        # Duplicate-free but sparse
        ([1, 10, 20, 30, 40], 20, 2),     # Found
        ([1, 10, 20, 30, 40], 15, -1),    # Not found
        
        # Edge case: very large array (conceptual)
        (list(range(0, 1000, 2)), 500, 250),    # Found at middle
        (list(range(0, 1000, 2)), 999, -1),     # Not found (odd number)
        (list(range(0, 1000, 2)), 0, 0),        # First element
        (list(range(0, 1000, 2)), 998, 499),    # Last element
    ]
    
    print("Running Binary Search Tests...")
    print("=" * 50)
    
    passed = 0
    total = len(test_cases)
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = search(nums, target)
        status = "PASS" if result == expected else "FAIL"
        
        # Format array display for readability
        if len(nums) > 10:
            nums_str = f"[{nums[0]}, {nums[1]}, ..., {nums[-2]}, {nums[-1]}] (len={len(nums)})"
        else:
            nums_str = str(nums)
        
        print(f"Test {i:2d}: {status}")
        print(f"  Array: {nums_str}")
        print(f"  Target: {target}")
        print(f"  Expected: {expected}, Got: {result}")
        
        if result == expected:
            passed += 1
        else:
            print(f"  ❌ FAILED!")
        print()
    
    print("=" * 50)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
    else:
        print(f"❌ {total - passed} tests failed")

# Run the tests
if __name__ == "__main__":
    run_tests()
