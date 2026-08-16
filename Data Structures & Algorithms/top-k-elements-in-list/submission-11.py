class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = defaultdict(int)

        for i in nums:
            seen[i] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key, v in seen.items():
            buckets[v].append(key)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
