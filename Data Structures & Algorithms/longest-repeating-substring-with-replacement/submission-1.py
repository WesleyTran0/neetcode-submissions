class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        mp = defaultdict(int)
        l = 0
        maxF = 0

        for r in range(len(s)):
            mp[s[r]] += 1
            maxF = max(maxF, mp[s[r]])

            while (r - l + 1) - maxF > k:
                mp[s[l]] -= 1
                l += 1

        
        return r - l + 1