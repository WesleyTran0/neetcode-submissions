class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in nums:
            if i in seen.keys():
                return True
            else:
                seen[i] = 1
        
        return False
