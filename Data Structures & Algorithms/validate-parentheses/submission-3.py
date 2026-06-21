class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"}" : "{", ")" : "(", "]" : "["}

        for char in s:
            if char in pair.keys():
                if stack and stack[-1] == pair[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False        