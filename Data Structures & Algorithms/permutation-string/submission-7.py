class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        oneFreq = defaultdict(int)
        for i in s1:
            oneFreq[i] += 1
        
        print(oneFreq)
        l = 0
        wndwFreqs = defaultdict(int)
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                wndwFreqs[s2[l]] -= 1
                if wndwFreqs[s2[l]] == 0:
                    del wndwFreqs[s2[l]]
                l += 1
            wndwFreqs[s2[r]] += 1
            if wndwFreqs.items() == oneFreq.items():
                return True
        return False
