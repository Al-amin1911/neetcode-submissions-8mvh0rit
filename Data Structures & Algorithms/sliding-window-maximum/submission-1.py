class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        arr_end = k-1
        l, r = 0, arr_end
        while r < len(nums):
            max_num = float("-inf")
            for item in set(nums[l:r+1]):
                max_num = max(max_num, item)
            ans.append(max_num)
            l += 1
            r += 1
        return ans
