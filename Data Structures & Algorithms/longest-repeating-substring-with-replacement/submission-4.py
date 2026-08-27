class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        best = 0

        l = 0
        maxF = 0
        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxF = max(maxF, mp[s[r]])
            while (r - l + 1) - maxF > k:
                mp[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best