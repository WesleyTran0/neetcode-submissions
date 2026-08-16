class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        s_start = 0
        res = []

        while s_start < len(s):
            l = ""
            while s[s_start] != "#":
                l += s[s_start]
                s_start += 1
            
            res.append(s[s_start + 1:s_start + 1 + int(l)])
            s_start = s_start + 1 + int(l)
        
        return res

