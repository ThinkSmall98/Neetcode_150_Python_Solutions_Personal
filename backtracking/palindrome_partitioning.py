# Time: O(n * 2^n) where n = len of str, Space: O(n)
class Solution:
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part[:]) # deep copy
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i: j + 1])
                    dfs(j + 1) # want to do j, not i
                    part.pop()
        dfs(0)
        return res
