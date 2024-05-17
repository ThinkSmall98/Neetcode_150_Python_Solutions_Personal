# Time Complexity: O(N*3^L)where N = # of cells in the board and L = len of the word to be matched
# Space Complexity: O(L) where L = len of word to be matched
from collections import Counter, defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # (r, c) 

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r >= ROWS or c >= COLS or
                (r, c) in path or 
                word[i] != board[r][c] or
                min(r, c) < 0):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or 
                    dfs(r - 1, c, i + 1) or 
                    dfs(r, c - 1, i + 1) or 
                    dfs(r, c + 1, i + 1)
                  )
            path.remove((r, c)) # backtrack
            return res 
        # reverse string if freq of 1st letter greater than last let
        count = Counter(letter for row in board for letter in row)
        if count[0] > count[-1]:
            count = count[::-1]
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
