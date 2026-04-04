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
        s = s.strip()
        word = []
        if not s:
            return []
        i = 0
        print(s)
        # for i in range(len(s)-1):
        #     if s[i].isnumeric() and s[i+1] == "#":
        #         count = int(s[i])
        #         pos = i+2
        #         strs = s[pos:pos+count]
        #         word.append(strs)      
        while i < len(s)-1:
            j = i+1
            print(f'loop iteration: {i}')
            while s[i].isnumeric() and s[j] != "#":
                    j += 1
            if s[i].isnumeric() and s[j] == "#":
                print(s[i:j])
                count = int(s[i:j])
                pos = j+1
                strs = s[pos:pos+count]
                print(strs)
                word.append(strs)
                i = pos+count
            # for j in range(i+1, len(s)-1):
            #     if s[i].isnumeric() and s[j] != "#":
            #         j += 1
            #     if s[i].isnumeric() and s[j] == "#":
            #         print(s[i:j])
            #         count = int(s[i:j])
            #         pos = j+1
            #         strs = s[pos:pos+count]
            #         word.append(strs)
            #         i = j
                                 
        return word
        pass