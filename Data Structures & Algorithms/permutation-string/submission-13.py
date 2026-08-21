class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        mp = {}
        for i in s1:
            mp[i] = 1 + mp.get(i, 0)
        
        wndw = {}
        l = 0
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                wndw[s2[l]] -= 1
                if wndw[s2[l]] == 0:
                    del wndw[s2[l]]
                l += 1
            
            wndw[s2[r]] = 1 + wndw.get(s2[r], 0)
            if wndw.items() == mp.items():
                return True
        return False