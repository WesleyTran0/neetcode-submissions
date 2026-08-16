class Solution:

    def encode(self, strs: List[str]) -> str:
        done = ""
        for s in strs:
            done += str(len(s)) + "#" + s
        return done

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            start = i
            while s[start] != "#":
                start += 1
            
            l = int(s[i:start])

            res.append(s[start + 1:start + 1 + l])
            i = start + l + 1
        
        return res

