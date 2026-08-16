class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        seen_s = {}
        seen_t = {}

        for (idx, _) in enumerate(s):
            if s[idx] in seen_s:
                seen_s[s[idx]] += 1
            else:
                seen_s[s[idx]] = 1
            
            if t[idx] in seen_t:
                seen_t[t[idx]] += 1
            else:
                seen_t[t[idx]] = 1
            
        for key in seen_s:
            if (key not in seen_t) or seen_t[key] != seen_s[key]:
                return False

        return True