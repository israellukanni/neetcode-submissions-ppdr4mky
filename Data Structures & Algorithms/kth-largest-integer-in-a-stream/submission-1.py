class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        self.k = k


    def add(self, val: int) -> int:
        heapq.heappush(self.heap,-val)
        store = []
        while len(store) < self.k:
            store.append(heapq.heappop(self.heap))
        for s in store:
            heapq.heappush(self.heap,s)
        return -store[-1]
