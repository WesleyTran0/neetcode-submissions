class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strsToHash = defaultdict(list)
        
        for string in strs:
            count = [0] * 26
            for let in string:
                count[ord(let) - ord("a")] += 1
            
            if strsToHash.get(tuple(count)):
                strsToHash[tuple(count)].append(string) 
            else:
                strsToHash[tuple(count)] = [string]
        
        return list(strsToHash.values())