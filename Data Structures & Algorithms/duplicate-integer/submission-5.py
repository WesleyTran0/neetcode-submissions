class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = defaultdict(bool)
        for i in nums:
            if i in seen:
                return True
            seen[i] == True
        
        return False