class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        idx = 0
        
        while idx < len(s):
            num_end = idx
            while s[num_end] != "#": 
                j = idx
                num_end += 1
                
            count = int(s[idx:num_end])
            word = s[num_end + 1:num_end + 1 + count]
            result.append(word)
            idx = num_end + 1 + count

        return result
