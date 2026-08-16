class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        
        freqs = [[] for i in range(len(nums) + 1)]

        for num, count in seen.items():
            freqs[count].append(num)

        result = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                result.append(num)
                if len(result) == k:
                    return result
