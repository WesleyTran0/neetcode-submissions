class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # box sort

        returnArr = []
        freqs = [[] for i in range(len(nums) + 1)]
        freqList = {}

        for i in nums:
            freqList[i] = 1 + freqList.get(i, 0)
        
        for key, val in freqList.items():
            freqs[val].append(key)

        idx = len(freqs) - 1
        while len(returnArr) != k:
            if freqs[idx]:
                returnArr += freqs[idx]
            idx -= 1
        
        return returnArr