class Solution:

    """

    5#Hello5#World

    i = 0
    j = 2

    s[i + start:i + start + length]
    i = i + start + length

    """

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        
        i = 0
        s_start = 0
        res = []

        while len(s) > i:
            j = i
            length = ""
            while s[j] != "#":
                length += s[j]
                j += 1
            
            length = int(length)
            i = j + 1
            res.append(s[i:i + length])
            i = i + length
        
        return res

