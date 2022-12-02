# Time: O((m + n) * (log(m + n) * log(log(m+n)))^2) < O((m+n)^2)
# Space: O(1)
from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n -2) // (factorial(n-1) * factorial(m-1))

Combinatorics: P = n! / ((n-k)! * k!). n choose k
P = (h + v)! / (h! * v!)
 where h = m - 1 horizontal moves & v = n - 1 vertical moves.
so P = (m + n - 2)! /((m-1)! * (n-1)!)

# Time: O(n * m)
# Space: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
