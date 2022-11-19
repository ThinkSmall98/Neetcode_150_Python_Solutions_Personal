# Time Complexity: O(N^2*log⁡(N)). We may expand O(N^2) nodes, and each one requires O(log⁡N) time to perform the heap operations.
# Space Complexity: O(N^2). Max size of the heap.

from heapq import heappop, heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
            N = len(grid)
            visited = set()
            minH = [[grid[0][0], 0, 0]] # (time/max-height, r, c)
            directions = ((1,0),(-1,0),(0,1),(0,-1))

            visited.add((0, 0))
            while minH:
                t, r, c = heappop(minH)

                if r == N - 1 and c == N - 1:
                    return t
                for dr, dc in directions:
                    neiR, neiC = r + dr, c + dc
                    if (min(neiR, neiC) < 0 or max(neiR, neiC) == N or (neiR, neiC) in visited):
                        continue
                    visited.add((neiR, neiC))
                    heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

# Dijkstra's alg.
