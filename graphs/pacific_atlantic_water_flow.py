# Time: O(m*n) where m & n=dimensions of grid
# Space: O(m*n)
# DFS
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
# BFS
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: 
            return []
            
        ROWS, COLS = len(heights), len(heights[0])

        # Setup each queue with cells adjacent to their respective ocean
        pac_q = deque()
        atl_q = deque()
        for r in range(ROWS):
            pac_q.append((r, 0))
            atl_q.append((r, COLS - 1))
        for c in range(COLS):
            pac_q.append((0, c))
            atl_q.append((ROWS - 1, c))
        
        def bfs(queue):
            visited = set()
            while queue:
                (row, col) = queue.popleft()
                visited.add((row, col))
                for (x, y) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    new_row, new_col = row + x, col + y
                    # Check if the new cell is within bounds
                    if (min(new_row, new_col) < 0 or new_row == ROWS or new_col == COLS or
                        (new_row, new_col) in visited or heights[new_row][new_col] < heights[row][col]):
                        continue
                    # If we've gotten this far, that means the new cell is reachable
                    queue.append((new_row, new_col))
            return visited
        
        # Perform a BFS for each ocean to find all cells accessible by each ocean
        pac_set = bfs(pac_q)
        atl_set = bfs(atl_q)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pac_set.intersection(atl_set))
# Start from oceans and keep track of pacific & atlantic. Return intersection of both sets
