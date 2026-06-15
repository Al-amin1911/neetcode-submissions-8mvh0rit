class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This dictionary will store: { number: its_index }
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            # If the complement is already in our dictionary, we found the pair!
            if diff in seen:
                return [seen[diff], i]

            # Otherwise, record the current number and its index, then move on
            seen[num] = i