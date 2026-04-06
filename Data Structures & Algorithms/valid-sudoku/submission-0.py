class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {}
        column_hash = {}
        square_hash = {} 
        for index in range(len(board)):
            row_hash[index] = set([])
            column_hash[index] = set([])
            square_hash[index] = set([])
        # for coulumn in range(9):
        #     for row in range(9):
        #         num = board[row][column] 
        #         # Board formula
        #         pos = ((row//3)*3 + (col//3))
        #         # check if item in row, column or square hash
        #         # skip if num == "."
        #         if num == ".":
        #             continue
        #         if num in row_hash[row] or column_hash[col] or square_hash[pos]:
        #             return False
        #         # else add to hashes
        #         row_hash[row].add(num)
        #         column_hash[col].add(num)
        #         square_hash[pos].add(num)
        # return True

        for index in range(len(board)):
            for item in board[index]:
                if item == ".":
                    continue
                if item.isnumeric() and item not in row_hash[index] :
                    row_hash[index].add(item) 
                else:
                    return False               
            for item in board:
                if item[index] == ".":
                    continue
                if item[index].isnumeric() and item[index] not in column_hash[index]:
                    column_hash[index].add(item[index])
                else:
                    return False
            for row_pos in range(len(board[index])):
                row = board[index]
                col_pos = index
                pos = ((row_pos//3)*3 + (col_pos//3))
                if row[row_pos] == ".":
                    continue
                if row[row_pos].isnumeric() and row[row_pos] not in square_hash[pos]:
                    square_hash[pos].add(row[row_pos])
                else:
                    return False
        return True




