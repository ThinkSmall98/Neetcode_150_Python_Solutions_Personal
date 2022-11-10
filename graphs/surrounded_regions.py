# Time: O(m*n), Space: O(m * n)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r,c):
            if (min(r,c) < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            for (x,y) in ((1,0),(-1,0),(0,1),(0,-1)):
                new_r, new_c = x+r, y+c
                capture(new_r,new_c)
        # 1. Capture unsurrounded areas ("O" -> "T")
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and r in (0, ROWS - 1) or c in (0, COLS - 1)): # check edges
                    capture(r,c)
        # 2. Capture surround areas ("O" -> "X")
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # 3. Uncapture unsurrounded areas ("T" -> "O")
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
