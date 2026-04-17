class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones:
            return 0
        import heapq
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) >= 2:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first - second > 0:
                heapq.heappush(heap, -(first-second))
        return -heapq.heappop(heap) if heap else 0
