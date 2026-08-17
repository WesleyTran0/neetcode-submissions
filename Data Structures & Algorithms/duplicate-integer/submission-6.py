class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mp = defaultdict(bool)
        for i in nums:
            if mp[i]:
                return True
            mp[i] = True
        return False