class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if len(nums) == 1 and nums[l] == target:
            return l
        # if len(nums) == 2:
        #     if nums[l] == target:
        #         return l
        #     elif nums[r] == target:
        #         return r
        while l < r:
            mid = (r+l)//2
            if (nums[mid] > nums[r] and (target > nums[mid] or target <= nums[r])) or (nums[mid] < nums[r] and (target > nums[mid] and target<= nums[r])):
                l = mid+1
            else:
                r = mid

            if nums[r] == target:
                return r                

        return -1
                

        