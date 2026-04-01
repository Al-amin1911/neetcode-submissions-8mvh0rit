class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = set(s)
        set_t = set(t)
        s_dict = {}
        t_dict = {}
        for i in set_s:
            s_dict[i] = s.count(i)
        for j in set_t:
            t_dict[j] = t.count(j)

        return s_dict == t_dict
         
        