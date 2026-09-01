class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqs = defaultdict(list)
        for i in strs:
            freq = [0] * 26
            for s in i:
                freq[ord(s) - ord('a')] += 1
            
            key = tuple(freq)
            freqs[key].append(i)
        
        return list(freqs.values())
