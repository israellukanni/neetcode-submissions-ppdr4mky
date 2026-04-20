class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        newNums = [-n for n in nums]
        heapq.heapify(newNums)

        for _ in range(k-1):
            heapq.heappop(newNums)
        return -newNums[0]