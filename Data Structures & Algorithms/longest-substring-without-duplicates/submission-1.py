class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hash_set = defaultdict(set)
        count = 0
        if len(s) == 1:
            return 1
        while r < len(s):
            if s[r] not in hash_set['current']:
                hash_set['current'].add(s[r])
                print(hash_set['current'])
                r += 1
                count = max(count, len(hash_set['current']))
            else:
                hash_set['current'].remove(s[l])
                l += 1
        return count

