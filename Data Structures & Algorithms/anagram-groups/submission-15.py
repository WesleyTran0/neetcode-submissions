class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for i in strs:
            freq = [0] * 27
            for s in i:
                freq[ord('a') - ord(s)] += 1
            buckets[tuple(freq)].append(i)
        
        return list(buckets.values())