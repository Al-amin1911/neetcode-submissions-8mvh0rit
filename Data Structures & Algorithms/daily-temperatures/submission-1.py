class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        i = 0
        while i < len(temperatures):
            # compare current element with elements in stack while not empty
            # apply only when incoming element greater than topmost element
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # set the result of the pos(popped element) == (pos.incoming - pos.outgoing)
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            i += 1
        return result
            


                        

