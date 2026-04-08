class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        curr_max = float('-inf')
        while l < r:
            vol = (r-l) * min(heights[l],heights[r])
            if curr_max < vol:
                curr_max = vol
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        return curr_max