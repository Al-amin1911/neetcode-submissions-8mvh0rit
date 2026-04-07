class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            target = -(nums[i])
            j,k = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] == target:
                    arr = [nums[i], nums[j], nums[k]]
                    if arr not in res:
                        res.append(arr)
                    j += 1
                    k -= 1
        return res          

        