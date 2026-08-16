class Solution:

    def encode(self, strs: List[str]) -> str:

        returnStr = ""

        for s in strs:
            sLen = len(s)
            returnStr += str(sLen) + ","
        
        returnStr += "#"

        for s in strs:
            returnStr += s
        
        return returnStr

    def decode(self, s: str) -> List[str]:

        lengths = []
        returnList = []

        count = 0
        while s[count] != "#":
            
            curNum = ""
            while s[count] != ",":
                curNum += s[count]
                count += 1 # next digit/number/char

            lengths.append(int(curNum))
            curNum = ""
            count += 1 # past the comma
        
        count += 1 # past the # 
        for l in lengths:
            returnList.append(s[count:count + l])
            count += l
        
        return returnList