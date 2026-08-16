class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        sdict = {}
        tdict = {}

        for i in range(len(s)):
            if sdict.get(s[i]):
                sdict[s[i]] += 1
            else:
                sdict[s[i]] = 1
            if tdict.get(t[i]):
                tdict[t[i]] += 1
            else:
                tdict[t[i]] = 1
            
        return sdict == tdict