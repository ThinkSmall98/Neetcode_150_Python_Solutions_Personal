# Time: O(m * n) where m & n = dimensions of grid , Space: O(min(m,n))
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() # (r, c)

        def bfs(r, c):
            q = deque()
            # add to queue & to visited
            q.append((r, c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                directions = ((1,0),(-1,0),(0,1),(0,-1))
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r != ROWS and c != COLS and
                        min(r, c) >= 0 and
                        (r,c) not in visited and
                        grid[r][c] == '1' ):
                        # add to queue & to visited
                        q.append((r, c))
                        visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        return islands

