class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        before_stack  = []
        after_stack = []
        max_across = float('-inf')
        max_single = float('-inf')
        l = 0
        while l < len(heights):
            before_stack  = []
            after_stack = []
            max_single = max(max_single, heights[l])
            area_across = heights[l]

            if l >= 1:
                before_stack.extend(heights[:(l)])

            if l != len(heights)-1:
                after_stack.extend(heights[:l:-1])

            while before_stack and before_stack[-1] >= heights[l]:
                area_across += heights[l]
                before_stack.pop()

            while after_stack and after_stack[-1] >= heights[l]:
                area_across += heights[l]
                after_stack.pop()
            max_across = max(max_across, area_across)
            l += 1
        return max(max_across, max_single)


        