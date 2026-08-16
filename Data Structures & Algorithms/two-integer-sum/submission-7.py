class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = defaultdict(int)
        for i, val in enumerate(nums):
            if val in seen:
                return [seen[val], i]
            
            seen[target - val] = i
        
        print(seen)
        return []
