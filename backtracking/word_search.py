# Time Complexity: O(N*3^L)where N = # of cells in the board and L = len of the word to be matched
# Space Complexity: O(L) where L = len of word to be matched
from collections import defaultdict, Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # (x, y)

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r >= ROWS or c >= COLS or 
                (r, c) in path or 
                word[i] != board[r][c] or 
                min(r, c) < 0):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1) or 
                dfs(r - 1, c, i + 1) or 
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            path.remove((r,c)) # backtrack
            return res
        # TLE error: reverse word if freq of 1st letter greater than last letter
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False
