# Time: O(len(s) * len(wordDict))
# Space: O(len(s))
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: # stop word for loop and move onto next i
                    break
        return dp[0]


# BFS
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        q = deque([0])
        seen = set()
        len_s = len(s)

        while q:
            start = q.popleft()
            if start == len(s):
                return True
            for end in range(start + 1, len_s + 1):
                if end in seen:
                    continue
                if s[start: end] in words:
                    q.append(end)
                    seen.add(end)
        return False
