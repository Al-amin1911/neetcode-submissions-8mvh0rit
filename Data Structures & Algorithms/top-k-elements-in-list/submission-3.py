from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        nums = sorted(nums, key = lambda x: counts[x], reverse = True)
        output = []
        print(nums)
        for num in nums:
            if num in output:
                pass
            else:
                output.append(num)
                k -= 1
                if k == 0:
                    break
        return output
        