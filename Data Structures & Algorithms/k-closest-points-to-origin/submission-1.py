class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        # print(points)
        for point in points:
            x,y = point
            calc = math.sqrt((x**2) + (y**2))
            # if heap and calc <= heap[0]:
            heapq.heappush(heap,(calc,[x,y]))
        # store = heap[0][0]
        answer = []

        while heap and len(answer)<k:
            answer.append(heapq.heappop(heap)[1])
        return answer