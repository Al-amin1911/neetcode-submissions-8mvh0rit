class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)        

    def pop(self) -> None:
        self.stack.pop()        

    def top(self) -> int:
       return self.stack[-1]        

    def getMin(self) -> int:
        min_value = float('inf')
        for item in self.stack:
            if item < min_value:
                min_value = item
        return min_value

        
        
