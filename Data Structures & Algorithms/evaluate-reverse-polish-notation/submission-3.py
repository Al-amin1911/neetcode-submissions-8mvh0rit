class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+', '-', '*', '/'}
        stack = []
        r = 0
        while r < len(tokens):
            print(r)
            #if pointer is not and operand
            if tokens[r] not in operands:
                stack.append(int(tokens[r]))
            #else, calculate for res for the last 2 values and pop them
            elif tokens[r] in operands and len(stack)>=2:
                print(f"incoming:{stack}, operand: {tokens[r]}")
                if tokens[r] == '+':
                    temp = stack[-2] + stack[-1]
                if tokens[r] == '-':
                        temp = stack[-2] - stack[-1]
                if tokens[r] == '*':
                    temp = stack[-2] * stack[-1]
                if tokens[r] == '/':
                    temp = int(stack[-2] / stack[-1])                
                stack.pop()
                stack.pop()
                stack.append(temp)
                print(f"outgoing:{stack}")
            r += 1
        return stack[0]




        