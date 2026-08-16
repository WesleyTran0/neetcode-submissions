class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = defaultdict(list)

        for s in strs:

            key = [0] * 26
            for l in s:
                key[ord(l) - ord('a')] += 1
            
            seen[tuple(key)].append(s)

        return list(seen.values())