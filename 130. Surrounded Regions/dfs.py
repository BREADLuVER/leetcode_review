class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row, col = len(board), len(board[0])
        if row <= 2 or col <= 2:
            return
        
        for r in range(row):
            self.dfs(board, r, 0, row, col)
            self.dfs(board, r, col-1, row, col)
        for c in range(col):
            self.dfs(board, 0, c, row, col)
            self.dfs(board, row-1, c, row, col)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "I":
                    board[r][c] = "O"

    def dfs(self, board, r, c, row, col):
        if 0<=r<row and 0<=c<col and board[r][c] == "O":
            board[r][c] = "I"
            self.dfs(board, r, c+1, row, col)
            self.dfs(board, r, c-1, row, col)            
            self.dfs(board, r-1, c, row, col)            
            self.dfs(board, r+1, c, row, col)  