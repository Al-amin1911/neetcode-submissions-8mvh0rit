from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        char_count_s1= {}
        char_count_s2 = defaultdict(dict)
        for char in s1:
            if char not in char_count_s1.keys():
                char_count_s1[char] = 1
            else:
                char_count_s1[char] += 1
        while l < len(s2)-len(s1)+1:
            r = l+len(s1)
            print(l, r)
            for char in s2[l:r]:
                if char not in char_count_s2[l].keys():
                    char_count_s2[l][char] = 1
                else:
                    char_count_s2[l][char] += 1
            print(char_count_s1, char_count_s2[l])
            if char_count_s1 == char_count_s2[l]:
                return True
            l += 1
        return False
        