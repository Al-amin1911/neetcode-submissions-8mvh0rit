class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        # char_freq = defaultdict(dict)
        char_freq = {}
        max_length = 0
        while r < len(s):
            max_freq = 0
            # for char in range(len(window_size)):
            #     if char not in char_freq[window_size]:
            #         char_freq[window_size][char] = 1
            #     else:
            #         char_freq[window_size][char] += 1
            if s[r] not in char_freq:
                char_freq[s[r]] = 1
            else:
                char_freq[s[r]] += 1
            window = (r-l) + 1 
            max_freq = max(char_freq.values())
            if window - max_freq <= k:
                max_length = max(max_length, window)
                r += 1
            else:
                while window - max_freq > k:
                    char_freq[s[l]] -= 1
                    max_freq = max(char_freq.values())
                    l += 1
                    window = (r-l) + 1 
                max_length = max(max_length, window)
                r += 1

        return max_length 
            
                    




        