class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        oneFreq = {}
        for s in s1:
            oneFreq[s] = 1 + oneFreq.get(s, 0)
        
        print(oneFreq)
        twoFreq = {}
        l = 0
        for r in range(len(s2)):
            twoFreq[s2[r]] = 1 + twoFreq.get(s2[r], 0)
            if (r - l + 1) > len(s1):
                twoFreq[s2[l]] -= 1
                if twoFreq[s2[l]] == 0:
                    del twoFreq[s2[l]]
                l += 1

            if twoFreq == oneFreq:
                return True


        return False