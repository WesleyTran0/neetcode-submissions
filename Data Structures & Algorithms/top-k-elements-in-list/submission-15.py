class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = {}
        for i in nums:
            freqs[i] = 1 + freqs.get(i, 0)
        
        boxes = [[] for i in range(len(nums) + 1)] 
        for key, val in freqs.items():
            boxes[val].append(key)
        
        res = []
        for i in range(len(boxes) - 1, -1, -1):
            for num in boxes[i]:
                res.append(num)
                if len(res) == k:
                    return res
                