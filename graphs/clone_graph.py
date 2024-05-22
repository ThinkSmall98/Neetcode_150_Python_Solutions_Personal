"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Time: O(n+m) where n = # of nodes & m = # of edges
# Space: O(n)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            node_copy = Node(val = node.val)
            oldToNew[node] = node_copy
            for neigh in node.neighbors:
                # need to run dfs on neigh to get copy of that neigh
                node_copy.neighbors.append(dfs(neigh))
            return node_copy

        return dfs(node) if node else None
