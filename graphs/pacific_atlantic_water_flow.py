# Time: O(m*n) where m & n=dimensions of grid
# Space: O(m*n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if ((r,c) in visited or min(r,c) < 0 
                or r == ROWS or c == COLS 
                or heights[r][c] < prevHeight):
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])


        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS -1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        res = list(pac.intersection(atl))
        return res

# Start from oceans and keep track of pacific & atlantic. Return intersection of both sets
