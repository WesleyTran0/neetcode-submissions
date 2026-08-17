class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for s in strs:
            freqs = [0 for i in range(26)]
            for i in s:
                freqs[ord(i) - ord('a')] += 1
            mp[tuple(freqs)].append(s)
        
        return list(mp.values())
        
