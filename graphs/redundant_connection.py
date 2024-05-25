class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # len + 1 bc the nodes start at 1, not 0. Keep 0 empty
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def findRootParent(n):
            while n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n

        def union(n1, n2):
            p1, p2 = findRootParent(n1), findRootParent(n2)
            if p1 == p2: # redundant connection
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
