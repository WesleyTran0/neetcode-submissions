class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp = {}
        l = 0
        res = 0

        for idx, letter in enumerate(s):
            if letter in mp:
                l = max(l, mp[letter] + 1)
            mp[letter] = idx
            res = max(res, idx - l + 1)
        
        return res