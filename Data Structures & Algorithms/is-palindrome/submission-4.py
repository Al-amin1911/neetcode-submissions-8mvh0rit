class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_rev = "".join([s[i].lower() for i in range(len(s)-1, -1, -1) if s[i].isalnum()])
        s = "".join(filter(str.isalnum, s)).lower()
        print(s, s_rev)
        return  s == s_rev
        