class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]
        temp = nums[0]
        
        for i in range(1, len(nums)):
            res.append(temp)
            temp *= nums[i]
        
        temp = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        
        return res

