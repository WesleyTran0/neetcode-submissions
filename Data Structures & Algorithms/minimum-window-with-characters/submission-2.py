class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, wndw = {}, {}
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        
        has, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            wndw[s[r]] = 1 + wndw.get(s[r], 0)

            if s[r] in countT and wndw[s[r]] == countT[s[r]]:
                has += 1
            
            while has == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                wndw[s[l]] -= 1
                if s[l] in countT and wndw[s[l]] < countT[s[l]]:
                    has -= 1
                l += 1
        
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
            