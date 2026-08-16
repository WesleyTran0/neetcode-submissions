class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = defaultdict(list)
        
        for s in strs:
            cur = [0] * 26
            for let in s:
                cur[ord(let) - ord('a')] += 1
            
            seen[tuple(cur)].append(s)
        
        return list(seen.values())