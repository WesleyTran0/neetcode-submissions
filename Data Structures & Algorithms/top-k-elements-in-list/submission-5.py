class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = defaultdict(int)

        for i in nums:
            freqs[i] += 1

        rec = [[] for i in range(len(nums) + 1)]

        for num, v in freqs.items():
            rec[v].append(num)
        
        res = []
        for i in range(len(rec) - 1, -1, -1):
            for j in rec[i]:
                res.append(j)
                if len(res) == k:
                    return res