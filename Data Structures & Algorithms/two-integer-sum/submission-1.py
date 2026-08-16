class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        need = {}

        for i, v in enumerate(nums): 
            if v in need.keys():
                return [need[v], i]
            
            need[target - v] = i

        return []