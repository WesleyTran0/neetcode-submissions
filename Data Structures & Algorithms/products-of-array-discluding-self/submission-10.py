class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        temp = 1

        for i, val in enumerate(nums):
            res.append(temp)
            temp *= val
        
        temp = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        
        return res

        