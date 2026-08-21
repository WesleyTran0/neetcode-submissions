class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mpS = defaultdict(int)
        for i in s:
            mpS[i] += 1
        
        for i in t:
            if i not in t:
                return False
            mpS[i] -= 1
        
        for v in mpS.values():
            if v != 0:
                return False
        
        return True