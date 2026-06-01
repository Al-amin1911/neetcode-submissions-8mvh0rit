class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i <= len(matrix)-1:
            if matrix[i][-1] >= target:
                if matrix[i][-1] == target:
                    return True
                elif matrix[i][0] == target:
                    return True
                column = matrix[i]
                l,r = 0, len(column)-1
                while l <= r:
                    mid = (r+l)//2
                    if column[mid] == target:
                        return True
                    elif column[mid] > target:
                        r = mid - 1
                    elif column[mid] < target:
                        l = mid + 1
            i += 1
        return False
