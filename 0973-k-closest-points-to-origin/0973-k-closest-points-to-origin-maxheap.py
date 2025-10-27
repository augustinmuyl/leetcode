class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-(x ** 2 + y ** 2), [x, y]))
            else:
                heapq.heappushpop(maxHeap, (-(x ** 2 + y ** 2), [x, y]))

        return [i[1] for i in maxHeap]