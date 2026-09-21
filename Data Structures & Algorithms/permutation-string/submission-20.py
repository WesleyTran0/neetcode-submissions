class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        oneFreq = {}
        for i in s1:
            oneFreq[i] = 1 + oneFreq.get(i, 0)
        
        print(oneFreq)
        wndw = {}
        l = 0
        for r in range(len(s2)):
            wndw[s2[r]] = 1 + wndw.get(s2[r], 0)
            if wndw.items() == oneFreq.items():
                return True
            if r - l + 1 == len(s1):
                wndw[s2[l]] -= 1
                if wndw[s2[l]] == 0:
                    del wndw[s2[l]]
                l += 1
            
            print(wndw)
        
        return False
                