# Time complexity: O(E⋅α(n)).
# Iterating over every edge requires O(E) operations, and for every operation, we are performing the combine method which is O(α(n)), where α(n) is the inverse Ackermann function

# Space complexity: O(V)
# Storing immediate-parent of each vertex takes O(V) space. Storing the size of components also takes O(V) space

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # initialize each parent of a node to be itself
        parent = [i for i in range(n)]
        rank = [1] * n

        def findRootParent(n):
            while n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n

        def union(n1, n2):
            p1, p2 = findRootParent(n1), findRootParent(n2)
            if p1 == p2:
                return 0
            elif rank[p1] > rank[p2]: # p1 is parent of p2
                parent[p2] = p1
                rank[p1] += rank[p2]
            else: # p2 is parent of p1
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


