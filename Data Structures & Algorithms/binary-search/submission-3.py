class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
    
        while r >= l:
            mid_idx = l + ((r - l) // 2)
            
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] < target:
                l = mid_idx + 1
            else:
                r = mid_idx - 1
        
        return -1

