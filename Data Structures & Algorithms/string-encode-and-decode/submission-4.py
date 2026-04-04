class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            if not string:
                encoded_string+("")
            str_len = len(string)
            encoded_string += f'{str_len}' + '#' + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        word = []
        i = 0
        if not s:
            return word
        while i < len(s)-1:
            j = i+1
            while s[i].isnumeric() and s[j] != "#":
                    j += 1
            word_length = int(s[i:j])
            word_start = j+1
            word_end = word_start + word_length
            word.append(s[word_start : word_end])
            i = word_end                               
        return word
        pass