class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i <= len(matrix)-1:
            if matrix[i][-1] >= target:
                if matrix[i][-1] == target:
                    return True
                elif matrix[i][0] == target:
                    return True
                row_i = matrix[i]
                l,r = 0, len(row_i)-1
                while l <= r:
                    mid = (r+l)//2
                    if row_i[mid] == target:
                        return True
                    elif row_i[mid] > target:
                        r = mid - 1
                    elif row_i[mid] < target:
                        l = mid + 1
                return False
            i += 1
        return False
