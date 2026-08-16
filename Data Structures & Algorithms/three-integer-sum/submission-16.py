class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        trips = []
        nums.sort()
        for i, val in enumerate(nums):
            if val > 0:
                break

            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + val
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    trips.append([nums[l], nums[r], val])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return trips