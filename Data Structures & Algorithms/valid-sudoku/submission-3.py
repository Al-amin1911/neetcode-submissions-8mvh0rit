class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        column_hash = defaultdict(set)
        square_hash = defaultdict(set)

        for col in range(9):
            for row in range(9):
                num = board[col][row] 
                # Board formula
                pos = ((row//3)*3 + (col//3))
                # check if item in row, column or square hash
                # skip if num == "."
                if num == ".":
                    continue
                if num in row_hash[row] or num in column_hash[col] or num in square_hash[pos]:
                    return False
                # else add to hashes
                row_hash[row].add(num)
                column_hash[col].add(num)
                square_hash[pos].add(num)
        return True





