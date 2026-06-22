class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = ["+", "-", "*", "/"]
        stack = []

        for item in tokens:
            if item in operation:
                b = stack.pop()
                a = stack.pop()
                match item:
                    case "+":
                        stack.append(a+b)
                    case "-":
                        stack.append(a-b)
                    case "*":
                        stack.append(a*b)
                    case "/":
                        stack.append(int(a/b))                   

            else:
                stack.append(int(item))
            
        return stack[0]