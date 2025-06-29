class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = []
        i, j, k = 0, 1, 2
    
        while i < n - 2:
            while j < n - 1:
                while k < n:
                    temp_list = [nums[i], nums[j], nums[k]]
                    temp_list.sort()
                    if (nums[i] + nums[j] + nums[k] == 0) and (temp_list not in triplets):
                        triplets.append(temp_list)
                    k += 1
                j += 1
                k = j + 1 if j < n - 1 else n
            i += 1
            j = i + 1 if i < n - 2 else n
            k = j + 1 if j < n - 1 else n
        
        return triplets
    
# Example usage:
my_list = [1, 2, 3, 4]

print("Using nested while loops (pointer method):")
all_triplets1 = threeSum(my_list)
print(all_triplets1)

print("\nUsing iterative pointer method:")
all_triplets2 = find_all_triplets_iterative_pointer(my_list)
print(all_triplets2)

# Both should output: [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]

# Test with another example
test_list = ['a', 'b', 'c', 'd', 'e']
print(f"\nTriplets from {test_list}:")
triplets = threeSum(test_list)
for triplet in triplets:
    print(triplet)