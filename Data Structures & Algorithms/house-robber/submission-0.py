class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        bests = [0] * len(nums)
        bests[0] = nums[0]
        bests[1] = max(nums[0], nums[1])
    
        for i in range(2, len(nums)):
            bests[i] = max(bests[i - 1], nums[i] + bests[i - 2])
        
        return bests[-1]
