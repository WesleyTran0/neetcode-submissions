class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numHash = {}

        for num in nums:
            numHash[num] = 1 + numHash.get(num, 0)
        
        freqToNums = [[] for _ in range(len(nums) + 1)]

        for num in numHash:
            # append the num to its freq in the frqToNums array
            freqToNums[numHash[num]].append(num)
        
        returnList = []
        idx = len(nums)
        while len(returnList) < k:
            if freqToNums[idx]:
                returnList += freqToNums[idx]
            idx -= 1
        
        return returnList