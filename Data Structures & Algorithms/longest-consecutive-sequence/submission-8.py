class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        best = 0
        for i in nums:
            if not mp[i]:
                mp[i] = mp[i - 1] + mp[i + 1] + 1
                mp[i - mp[i - 1]] = mp[i]
                mp[i + mp[i + 1]] = mp[i]

            best = max(best, mp[i])
        
        return best