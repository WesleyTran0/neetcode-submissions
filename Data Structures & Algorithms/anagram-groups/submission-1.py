class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = defaultdict(list)
        
        for i, string in enumerate(strs):
            sorted_ver = "".join(sorted(string))
            seen[sorted_ver].append(i)
        
        result = []
        for k in seen.keys():
            anagram = []
            for i in seen[k]:
                anagram.append(strs[i])
            result.append(anagram)

        return result