class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = defaultdict(set)
        pos_seq = set()

        for num in nums:
            if num-1 in nums:
                continue
            pos_seq.add(num)
        
        print(pos_seq)
        
        i = 0
        length = 0
        while i < len(pos_seq):
            num = list(pos_seq)[i]
            while num in nums:
                seq[i].add(num)
                num = num + 1
            length = max(length, len(seq[i]))
            i += 1
        
        return length
            

        