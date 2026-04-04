class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy.remove(nums[i])
            total = 1
            for item in nums_copy:
                total *= item
            res.append(total)
        return res