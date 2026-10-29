class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums) // 2
        
        return min(self.findMin(nums[mid:]),
                   self.findMin(nums[:mid]))