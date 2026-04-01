class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = {}
        for i in range(len(nums)):
            num_pos[nums[i]] = i
        for i in range(len(nums)):
            remainder = target-nums[i]
            if remainder in nums and num_pos[remainder] != i:
                return [i, num_pos[remainder]]
                
        
            