class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(list)
        count = Counter(nums)

        for num in count:
            num_count[count[num]].append(num)
        res = []
        list_v = sorted(list(num_count.keys()))
        while k>0:
            max_v = list_v[-1]
            for item in num_count[max_v]:
                res.append(item)
                k -= 1
            list_v.remove(max_v)

        return res


        

        