class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        total = 0   
        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max: # no water trapped here
                    left_max = height[l]
                else:
                    total += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    total += right_max - height[r]
                r -= 1
        return total