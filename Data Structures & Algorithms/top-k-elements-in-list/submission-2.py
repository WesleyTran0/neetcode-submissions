class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1

        arr = []
        for num, count in seen.items():
            arr.append([count, num])
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
