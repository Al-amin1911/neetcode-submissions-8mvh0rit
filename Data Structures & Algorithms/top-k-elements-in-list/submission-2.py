class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frq = {}
        list_n = []
        for num in nums:
            if num not in num_frq.keys():
                num_frq[num] = 1
            num_frq[num] += 1
        print(num_frq)
        while k > 0:
            max_k = max(num_frq.values())
            for x in list(num_frq.keys()):
                if num_frq[x] == max_k:
                    list_n.append(x)
                    num_frq.pop(x)
                    k -= 1
        return list_n