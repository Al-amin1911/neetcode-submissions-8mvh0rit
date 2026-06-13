class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = sorted(nums)   

    def add(self, val: int) -> int:
        self.arr.append(val)
        heap = deque(sorted(self.arr)[-self.k:])
        if val > heap[0]:
            heap.append(val)
            heap = sorted(heap)
            if len(heap) > self.k:
                heap.pop()
        
        return heap[0]
        
        
        
