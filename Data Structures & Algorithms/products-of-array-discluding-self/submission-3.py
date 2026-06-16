class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        suffix = []

        if not nums:
            return []

        for num in nums:
            index = nums.index(num)
            total = 1
            for i in range(index+1, len(nums)):
                total *= nums[i]
            prefix.append(total)
            total = 1
            for i in range(0, index):
                total *= nums[i]
            suffix.append(total)

        return [prefix[i]*suffix[i] for i in range(len(nums))]    

        

    