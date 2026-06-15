class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        nums_rev = [-n for n in nums]
        heapq.heapify(nums_rev)
        val = 0
        while k > 0:
            val = heapq.heappop(nums_rev)
            k -= 1
        
        return -val
        