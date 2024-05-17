# Time Complexity: O(N*3^L)where N = # of cells in the board and L = len of the word to be matched
# Space Complexity: O(L) where L = len of word to be matched
from collections import Counter, defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # (r, c)

        def dfs(i, r, c):
            if i == len(word):
                return True
            if (r >= ROWS or c >= COLS or
                (r,c) in path or 
                word[i] != board[r][c] or
                min(r, c) < 0):
                return False
            # add (r, c) in path
            path.add((r,c))
            res = (dfs(i + 1, r + 1, c) or 
                    dfs(i + 1, r - 1, c) or 
                    dfs(i + 1, r, c + 1) or 
                    dfs(i + 1, r, c - 1) )
            # remove (r, c) from path
            path.remove((r, c))

            return res
        # reverse string if freq of 1st letter > last letter
        count = Counter(letter for row in board for letter in row)
        if count[0] > count[-1]:
            count[::-1]
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        return False
