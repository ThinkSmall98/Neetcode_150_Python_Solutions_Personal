# Time: O(m * n), Space: O(m * n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r,c):
            if (min(r,c) < 0 or r == ROWS or c == COLS 
                or grid[r][c] == 0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r , c +1) + dfs(r, c-1) 
        for i in range(ROWS):
            for j in range(COLS):
                max_area = max(max_area, dfs(i, j))
        return max_area
