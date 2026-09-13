class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        best = 0
        maxF = 0
        freqs = {}

        for r in range(len(s)):
            freqs[s[r]] = 1 + freqs.get(s[r], 0)
            maxF = max(freqs[s[r]], maxF)
            while (r - l + 1) - maxF > k:
                freqs[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best