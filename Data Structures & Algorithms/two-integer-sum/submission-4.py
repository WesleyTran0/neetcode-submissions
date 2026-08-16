class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        need = defaultdict(int)

        for i, val in enumerate(nums):
            print(need)
            if val in need:
                return [need[val], i]
            
            need[target - val] = i
        
        return []
        
