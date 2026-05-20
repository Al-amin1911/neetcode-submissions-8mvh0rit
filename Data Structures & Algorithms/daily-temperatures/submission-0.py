class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        if not temperatures:
            return 0
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.append(j-i)
                    break
                else:
                    continue
            if len(result) - 1 != i:
                result.append(0)
        return result
        

