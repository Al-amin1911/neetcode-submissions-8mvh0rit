class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = {}

        for i in range(len(nums)):
            remainder = target-nums[i]
            if remainder in num_pos.keys():
                return[num_pos[remainder], i]
            num_pos[nums[i]] = i
                
        
            