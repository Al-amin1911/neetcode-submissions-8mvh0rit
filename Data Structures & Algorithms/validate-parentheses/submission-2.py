class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []
        open_b = close_b = 0
        # at least 2 characters
        if len(s) %2 != 0:
            return False
        for item in s:
            if item in pair.keys():
                stack.append(item)
                open_b += 1
            elif stack and item in pair.values() and pair[stack[-1]] == item:
                stack.pop()
                close_b += 1
            else:
                return False
        if open_b != close_b:
            return False
        return True