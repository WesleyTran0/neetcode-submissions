class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        rec = [[] for i in range(len(nums) + 1)]

        for i in nums:
            freqs[i] = freqs.get(i, 0) + 1
        for num, v in freqs.items():
            rec[v].append(num)
        
        res = []
        for i in range(len(rec) - 1, 0, -1):
            for j in rec[i]:
                res.append(j)
                if len(res) == k:
                    return res
