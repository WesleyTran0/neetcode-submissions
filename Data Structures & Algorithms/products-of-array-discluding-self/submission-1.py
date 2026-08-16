class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # forward pass on res
        # pass from back 

        res = [1]
        mult = nums[0]

        for i in range(1, len(nums)):
            res.append(mult)
            mult *= nums[i]
        
        mult = nums[len(nums) - 1]
        print(len(nums))
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= mult
            mult *= nums[i]
        
        return res
            
            