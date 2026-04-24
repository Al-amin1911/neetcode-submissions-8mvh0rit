from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, res_len = "", float("inf")
        count_t = Counter(t)
        window = {}
        have, need = 0, len(count_t)
        l = 0
        for r in range(len(s)):
            c = s[r] 
            window[c] = window.get(c, 0)+1

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = s[l:r+1]
                    res_len = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        return res
                
                



            
        