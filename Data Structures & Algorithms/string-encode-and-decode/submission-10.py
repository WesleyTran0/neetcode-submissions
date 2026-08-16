class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        count = 0

        while count < len(s):
            s_start = count

            while s[s_start] != "#":
                s_start += 1
            
            l = int(s[count:s_start])

            word = s[s_start+1:s_start+1+l]
            res.append(word)
            count = s_start + l + 1


        return res
