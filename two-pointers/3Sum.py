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