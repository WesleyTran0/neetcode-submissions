class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = {}
        for i in t:
            freqT[i] = 1 + freqT.get(i, 0)
        
        cur = {}
        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(freqT)
        l = 0

        for r in range(len(s)):
            cur[s[r]] = cur.get(s[r], 0) + 1
            if s[r] in freqT and cur[s[r]] == freqT[s[r]]:
                have += 1
            
            if have == need:
                while have == need:
                    if r - l + 1 < resLen:
                        res = [l, r]
                        resLen = r - l + 1
                    
                    cur[s[l]] -= 1
                    if s[l] in freqT and cur[s[l]] < freqT[s[l]]:
                        have -= 1
                    l += 1

        res = s[res[0]:res[1] + 1]
        return res if resLen != float("infinity") else ""
