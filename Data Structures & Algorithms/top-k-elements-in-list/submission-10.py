class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = defaultdict(int)

        for n in nums:
            freqs[n] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for n, cnt in freqs.items():
            buckets[cnt].append(n)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return []