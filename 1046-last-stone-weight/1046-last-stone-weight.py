class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            if y != x:
                heapq.heappush(maxHeap, -(y-x))
        
        return -maxHeap[0] if maxHeap else 0