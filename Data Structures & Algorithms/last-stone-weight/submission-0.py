class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0        

        min_heap = []
        heapq.heapify(min_heap)

        # add elementes to heap in reverse
        for stone in stones:
            heapq.heappush(min_heap, -stone)

        while min_heap and len(min_heap) > 1:

            large = -heapq.heappop(min_heap)
            small = -heapq.heappop(min_heap)

            diff = large - small
            if diff != 0:
                heapq.heappush(min_heap, -diff)
            
        if min_heap: 
            return -min_heap[0] 
        else: 
            return 0