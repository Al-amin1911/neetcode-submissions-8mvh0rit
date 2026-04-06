class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        if not nums:
            return 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                count = 0
                curr = num
                while curr in nums:
                    count += 1
                    curr += 1
                max_count = max(max_count, count)

        return max_count
             

