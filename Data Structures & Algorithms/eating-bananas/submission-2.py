class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h must be atlest the len of the piles
        # if h is at least the len of the piles, the fatest time will be 1hour to a pile
        # i.e k == max banana in a pile, min_k = 1, doesnt guarantee 1 will satisfy the question
        m = max(piles)
        n = len(piles)
        max_k = m
        min_k = 1  
        best = max_k
        # iterate through the possible values of k obvi starting from 1 with max_k included
        while min_k <= max_k:
            # check if each pile can be eaten at rate i
            sum_so_far = 0
            mid_k = (max_k+min_k)//2
            for j in range(n):
                time = math.ceil(piles[j]/mid_k)
                sum_so_far += time
            if sum_so_far > h:
                min_k = mid_k+1
            else:
                max_k = mid_k-1
                best = mid_k
        return best


        