# Time complexity: O(E⋅α(n)).
# Iterating over every edge requires O(E) operations, and for every operation, we are performing the combine method which is O(α(n)), where α(n) is the inverse Ackermann function

# Space complexity: O(V)
# Storing immediate-parent of each vertex takes O(V) space. Storing the size of components also takes O(V) space

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
