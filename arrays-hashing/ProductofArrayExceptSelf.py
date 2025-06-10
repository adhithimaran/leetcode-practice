class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output where output[i] is product of all ele's but nums[i]
        output = []
        
        # divide each ele by this product to get output[i]
        for i in range(len(nums)):
            output.append(self.product(nums, i))

        return output

    def product(self, nums, idx):
        # returns product of all elements but idx ele
        product = 1
        for i in range(len(nums)):
            if (i != idx):
                product *= nums[i]
        return product