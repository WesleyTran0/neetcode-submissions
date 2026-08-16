class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = {}

        for i in nums:
            freqs[i] = freqs.get(i, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for num, count in freqs.items():
            buckets[count].append(num)
        
        res = []

        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res