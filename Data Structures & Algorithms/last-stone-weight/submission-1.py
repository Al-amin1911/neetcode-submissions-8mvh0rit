class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            val = stone1-stone2
            if stone1 != stone2:
                heapq.heappush(heap, val)
        return -heap[0] if heap else 0

        