class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        seen_s = {}
        seen_t = {}

        for (idx, _) in enumerate(s):
            seen_s[s[idx]] = 1 + seen_s.get(s[idx], 0)
            seen_t[t[idx]] = 1 + seen_t.get(t[idx], 0)
            
        return seen_s == seen_t