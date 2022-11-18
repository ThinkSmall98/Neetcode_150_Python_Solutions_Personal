# Time: O(E * log(V)) bc Djikstra's alg.
# Space complexity: O(E + V)
from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((w, v))

        minHeap =[(0, k)] # weight, node index
        visited = set()
        t = 0
        while minHeap:
            w1, n1 = heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)

            for w2, n2 in edges[n1]:
                if n2 not in visited:
                    heappush(minHeap, (w1 + w2, n2))
        return t if len(visited) == n else -1
