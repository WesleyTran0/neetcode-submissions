class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = defaultdict(int)

        for i, val  in enumerate(nums):
            if val in mp:
                return [mp[val], i]
            
            mp[target - val] = i
        
        return []
