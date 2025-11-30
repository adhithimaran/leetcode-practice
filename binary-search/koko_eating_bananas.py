import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search bounds
        left = 1  # minimum possible speed
        right = max(piles)  # maximum possible speed needed
        
        while left < right:
            mid = (left + right) // 2
            
            # Calculate total time needed at this speed
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)
            
            # If we can finish in time, try a slower speed
            if total_time <= h:
                right = mid
            else:
                # Too slow, need faster speed
                left = mid + 1
        
        return left

# Test the solution
solution = Solution()

# Test case 1
piles1 = [3, 6, 7, 11]
h1 = 8
print(f"Test 1: piles={piles1}, h={h1}")
print(f"Result: {solution.minEatingSpeed(piles1, h1)}")  # Expected: 4

# Test case 2
piles2 = [30, 11, 23, 4, 20]
h2 = 5
print(f"\nTest 2: piles={piles2}, h={h2}")
print(f"Result: {solution.minEatingSpeed(piles2, h2)}")  # Expected: 30