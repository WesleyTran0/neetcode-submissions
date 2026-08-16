class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # -4 -1 -1 0 1 2
        # target = 1 -> 0 2

        nums.sort()
        final = []
        for idx, num in enumerate(nums):

            if num > 0:
                break
            
            if idx > 0 and num == nums[idx - 1]:
                continue

            target = -1 * num
            
            l = idx + 1
            r = len(nums) - 1

            while l < r:

                if nums[l] + nums[r] == target:
                    final.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                       l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
        
        return final