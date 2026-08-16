class Solution:

    """
    use a delimiter

    use double delimiter to identify delimiter

    Hello/, World -> Hello//World
    Hello//, World -> 
    """

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        
        return result

    def decode(self, s: str) -> List[str]:
        
        result = []
        idx = 0
        count = 0
        while idx < len(s): 
            count_str = ""
            while s[idx] != "#":
                count_str += s[idx]
                idx += 1
            count = int(count_str)
            idx += 1 # increment past the "#"
            word = ""
            for i in range(count):
                word += s[idx + i]
            result.append(word)
            idx += count
        
        return result
