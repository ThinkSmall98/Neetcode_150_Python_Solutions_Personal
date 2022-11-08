# Time: O(n+m) where n = # of nodes & m = # of edges
# Space: O(n)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(val = node.val)
            oldToNew[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            return copy
        return dfs(node) if node else None
