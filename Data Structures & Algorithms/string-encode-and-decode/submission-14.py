class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        s_start = 0
        i = 0
        while i < len(s):
            l = ""
            while s[s_start] != "#":
                l += s[s_start]
                s_start += 1
            i = s_start

            res.append(s[i + 1:i + int(l) + 1])

            i += int(l) + 1
            s_start = i
        
        return res
            
