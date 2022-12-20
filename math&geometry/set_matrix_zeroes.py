# Time: O(m * n)
# Space: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        # update rest of matrix based on top row and left col
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        # update left col
        for r in range(1, ROWS):
            if matrix[0][0] == 0:
                matrix[r][0] = 0
        # update top row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
