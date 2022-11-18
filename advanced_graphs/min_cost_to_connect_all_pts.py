# N = #  of points in the input array.
# Time complexity: O(N^2⋅log⁡(N))
from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        # Prim's
        res = 0
        visited = set()
        minH = [[0, 0]] # [cost, point]
        while len(visited) < N:
            cost, i = heappop(minH)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heappush(minH, [neiCost,nei])
        return res
