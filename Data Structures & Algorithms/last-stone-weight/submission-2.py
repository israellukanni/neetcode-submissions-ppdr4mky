class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x,y = -heapq.heappop(heap), -heapq.heappop(heap)
            
            if x > y:
                heapq.heappush(heap,-(x-y))
        return 0 if not heap else -heap[0]
