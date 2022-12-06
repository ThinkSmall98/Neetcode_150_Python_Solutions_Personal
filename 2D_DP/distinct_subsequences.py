# Time: O(m * n)
# Space: O(m * n)
class Solution:
    # Recursive + memoization
    def numDistinct(self, s: str, t: str) -> int:
        cache = {} # # (i, j) = number

        def dfs(i, j):
            M, N = len(s), len(t)
            if j == N or i == M: 
                return int(j == N) # whether or not we've completed str t
            if (i, j) in cache:
                return cache[(i, j)]
            # always make this call 
            cache[(i,j)] = dfs(i + 1, j)

            if s[i] == t[j]:
                cache[(i,j)] += dfs(i + 1, j + 1) 
                
            return cache[(i,j)]
        return dfs(0, 0)
    
    # 2D DP
    # Time: O(m * n)
    # Space: O(m * n)
    def numDistinct(self, s: str, t: str) -> int:
        ROWS, COLS = len(s) + 1, len(t) + 1

        dp = [[0] * COLS for _ in range(ROWS)]

        for i in range(ROWS):
            dp[i][0] = 1

        for i in range(1, ROWS):
            for j in range(1, COLS):
                dp[i][j] = dp[i - 1][j]

                if s[i - 1] == t[j - 1]: # Need to get prev values
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]
        
    # 1D dp
    # Time: O(m * n)
    # Space: O(n)
    def numDistinct(self, s: str, t: str) -> int:
        ROWS, COLS = len(s) + 1, len(t) + 1

        dp = [0] * COLS
        dp[0] = 1

        for i in range(1, ROWS):
            for j in range(COLS - 1, 0, -1):
                if s[i - 1] == t[j - 1]: # Need to get prev values
                    dp[j] += dp[j - 1]
        return dp[-1]
