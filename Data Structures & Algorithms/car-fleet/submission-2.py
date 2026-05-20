class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(list(zip(position, speed)), key = lambda x: x[0], reverse = True)
        time = [((target- item[0])/item[1]) for item in pairs]
        stack = []
        res = 1
        print(pairs, time)
        for i in range(len(pairs)) :
            while stack and time[i] > time[stack[0]]:
                stack.clear()
                res += 1
            stack.append(i)
        return res


        

