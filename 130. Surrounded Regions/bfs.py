class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        row, col = len(board), len(board[0])
        if row <= 2 or col <= 2:
            return
        
        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col and board[r][c] == 'O':
                board[r][c] = 'I'
                stack.append((r + 1, c))
                stack.append((r - 1, c))
                stack.append((r, c + 1))
                stack.append((r, c - 1))

        stack = []
        for r in range(row):
            stack.append((r, 0))
            stack.append((r, col - 1))
        for c in range(col):
            stack.append((0, c))
            stack.append((row - 1, c))
        
        while stack:
            r, c = stack.pop()
            dfs(r, c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'I':
                    board[r][c] = 'O'
