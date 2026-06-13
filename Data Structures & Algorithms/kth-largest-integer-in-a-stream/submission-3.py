class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = sorted(nums)   

        heapq.heapify(self.heap)

        # 2. Chop down the heap until only the k largest elements remain.
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # 1. Push the new value onto our min-heap. Time: O(log k)
        heapq.heappush(self.heap, val)

        # 2. If we exceed size k, throw away the smallest element. Time: O(log k)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # 3. The top of a min-heap is always the smallest element currently inside it.
        # In a room of the 'k' largest elements, the smallest one is the Kth largest overall!
        return self.heap[0]
        
        
        
