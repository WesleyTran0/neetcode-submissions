class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Vals = {}
        for s in s1:
            s1Vals[s] = 1 + s1Vals.get(s, 0)
        print(s1Vals)
        
        l = 0
        wndwVals = {}
        for r in range(len(s2)):
            if r - l + 1> len(s1):
                wndwVals[s2[l]] -= 1
                if wndwVals[s2[l]] == 0:
                    del wndwVals[s2[l]]
                l += 1
            wndwVals[s2[r]] = 1 + wndwVals.get(s2[r], 0)
            print(wndwVals)
            if wndwVals.items() == s1Vals.items():
                return True
        return False