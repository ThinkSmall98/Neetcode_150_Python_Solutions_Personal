# Time: O(m * n) where m = len(s) & n = len(p)
# Space: O(m * n) 
class Solution:
    # Top-down memoization
    def isMatch(self, s: str, p: str) -> bool:
        cache = {} # (i, j) where i = index of s & j = index of p

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if (j + 1) < len(p) and p[j + 1] == '*':
                cache[(i, j)] = (dfs(i, j + 2) or  # don't use at all
                                (match and dfs(i + 1, j))) # use *
            elif match:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = False
            return cache[(i, j)]
        return dfs(0, 0)
