class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        res = defaultdict(list)

        for word in strs:

            cache = [0] * 26

            for w in word:
                cache[ord(w) - ord('a')] +=1
            
            res[tuple(cache)].append(word)
        
        return list(res.values())
            



        
        