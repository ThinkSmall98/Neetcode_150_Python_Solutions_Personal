from collections import defaultdict
class Solution:
    # Time: O(n^2) = O(9*9) = O(81) = O(1)
    # Space: O(n^2) = O(1). We need 3n arrays each with len(n)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                elif val in rows[r] or val in cols[c] or val in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r//3, c//3)].add(val)
        return True
