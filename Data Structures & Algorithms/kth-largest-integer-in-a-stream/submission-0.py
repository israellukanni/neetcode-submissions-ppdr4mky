class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.k = k
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        store = []
        heapq.heappush(self.heap,-val)
        while len(store) < self.k:
            store.append(heapq.heappop(self.heap))
        for s in store:
            heapq.heappush(self.heap,s)
        return -store[-1]
        
