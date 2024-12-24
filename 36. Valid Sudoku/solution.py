from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid_dict = defaultdict(list)
        # check rows
        for row in board:
            if len(set(row)) < (10 - row.count(".")):
                return False
        # check columns
        for i in range(len(board)):
            col = [board[x][i] for x in range(len(board))]
            if len(set(col)) < (10 - col.count(".")):
                return False
        # check boxes
        for i in range(len(board)):
            for j in range(len(board)):
                grid_dict[(i//3),(j//3)] += board[i][j]
            
        for box in grid_dict.values():
            if len(set(box)) < (10 - box.count(".")):
                return False

        return True

board = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))