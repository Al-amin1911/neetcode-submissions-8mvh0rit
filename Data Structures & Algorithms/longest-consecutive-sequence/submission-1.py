class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count_list = []
        if not nums:
            return 0
        nums = sorted(nums)
        i = 0
        while i < len(nums):
            count = 1
            current = nums[i]
            for num in nums:
                if num == current + 1:
                    count += 1
                    current = num
            count_list.append(count) 
            i += 1  
        return max(count_list)     
