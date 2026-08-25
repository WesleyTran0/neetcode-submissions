class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mp = defaultdict(int)
        best = 0

        for n in nums:
            if not mp[n]:
                mp[n] = mp[n - 1] + mp[n + 1] + 1
                mp[n - mp[n - 1]] = mp[n]
                mp[n + mp[n + 1]] = mp[n]

                best = max(best, mp[n])
        
        return best
