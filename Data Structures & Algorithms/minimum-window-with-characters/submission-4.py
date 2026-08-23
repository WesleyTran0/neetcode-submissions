class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        countT, wndw = {}, {}
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        
        l = 0
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            wndw[s[r]] = 1 + wndw.get(s[r], 0)
            if s[r] in countT and countT[s[r]] == wndw[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                    
                wndw[s[l]] -= 1
                if s[l] in countT and wndw[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""


