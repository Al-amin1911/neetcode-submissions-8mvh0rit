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
            if s[i].isnumeric() and s[j] == "#":
                count = int(s[i:j])
                pos = j+1
                strs = s[pos:pos+count]
                word.append(strs)
                i = pos+count                                 
        return word
        pass