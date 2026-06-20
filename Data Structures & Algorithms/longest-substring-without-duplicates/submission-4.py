class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash_m = {}
        arr = []
        max_seq = 0

        for char in s:
            if char not in arr:
                arr.append(char)
            else:
                max_seq = max(max_seq, len(arr))
                char_index = arr.index(char)
                arr = arr[char_index+1:]
                arr.append(char)
        
        return max(max_seq, len(arr))
