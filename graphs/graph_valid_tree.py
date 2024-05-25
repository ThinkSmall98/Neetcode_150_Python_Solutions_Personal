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
'''
Depth-first search is a classic graph-traversal algorithm that can be used to check for both of these conditions:

G is fully connected iff, we started a depth-first search from a single source and discovered all nodes in G during it.
G contains no cycles iff, the depth-first search never goes back to an already discovered node. 
We need to be careful though not to count trivial cycles of the form A → B → A that occur with most implementations of undirected edges.'''
