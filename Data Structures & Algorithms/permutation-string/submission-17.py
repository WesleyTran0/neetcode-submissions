class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = {}
        for i in s1:
            mp[i] = mp.get(i, 0) + 1
        
        mp2 = {}
        l = 0
        for r in range(len(s2)):
            while (r - l + 1) > len(s1):
                mp2[s2[l]] -= 1
                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]
                l += 1
            mp2[s2[r]] = 1 + mp2.get(s2[r], 0)
            if mp2 == mp:
                return True
        return False