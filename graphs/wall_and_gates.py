# Time: O(m*n), Space: O(m*n)
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                rooms[row][col] = dist
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    r, c = dr + row, dc + col
                    if (min(r,c) < 0 or r == ROWS or c == COLS or rooms[r][c] == -1 or (r,c) in visited):
                        continue
                    q.append((r,c))
                    visited.add((r,c))
            dist += 1
