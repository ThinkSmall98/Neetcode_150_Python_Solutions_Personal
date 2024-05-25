# Time: O(E + V), Space: O(E + V)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited = set()
        
        # see if there's a cycle
        def dfs(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)
            for next in adj[curr]:
                if next == prev:
                    continue
                if not dfs(next, curr):
                    return False
            return True

        no_cycle = dfs(0, -1)
        all_connected_nodes = len(visited) == n
        return no_cycle and all_connected_nodes

# Check 2 things:
# 1. Path in b/w every node. num of nodes visited = nodes in tree
# 2. Make sure no cycle
