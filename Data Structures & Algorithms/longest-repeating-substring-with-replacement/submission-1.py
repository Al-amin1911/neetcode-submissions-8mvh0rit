class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_freq = {}
        max_freq = 0
        max_length = 0

        for r in range(len(s)):
            # expand window
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1
            max_freq = max(max_freq, char_freq[s[r]])

            # shrink if invalid
            while (r - l + 1) - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1

            # update result
            max_length = max(max_length, r - l + 1)

        return max_length
                    
                    




        