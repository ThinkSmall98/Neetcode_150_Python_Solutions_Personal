# Time: O(m*n), Space: O(m*n)
from collections import deque
class Solution:
    '''
    BFS bc we want to increment by 1 each time
    DFS goes too deep
    '''
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
            # go thru each level of the queue
            for _ in range(len(q)): 
                row, col = q.popleft()
                rooms[row][col] = dist
                for dr, dc in ((1,0), (-1,0),(0,1),(0,-1)):
                    r, c = dr + row, dc + col
                    if (r == ROWS or c == COLS or 
                        min(r,c) < 0 or 
                        (r,c) in visited or
                        rooms[r][c] == -1):
                        continue
                    q.append((r,c))
                    visited.add((r,c))
            dist += 1
 '''
 1. Initialize queue with gates
 2. Do BFS and keep a var. dist to find dist of gates
 3. Rewrite rooms array with dist values
 '''
