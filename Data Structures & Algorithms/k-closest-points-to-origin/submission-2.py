class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []

        for point in points:
            x,y = point
            dist = math.sqrt((x**2) + (y**2))
            heapq.heappush(heap,(dist,point))
        
        answer = []
        while heap and len(answer) < k:
            answer.append(heapq.heappop(heap)[1])
        return answer