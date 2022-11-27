# Time: O(n^2)
# Space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            if resLen > 0 and len(s) - 1 - i < resLen // 2:
                break
            # odd
            l, r = i, i
            res, resLen = self.isPali(s, l, r, resLen, res)
            # even
            l, r = i, i + 1
            res, resLen = self.isPali(s, l, r, resLen, res)
        return res
        
    def isPali(self, s, l, r, resLen = 0, res = ""):
        while l >= 0 and r < len(s) and s[r] == s[l]:
            if r + 1 - l > resLen:
                res = s[l: r + 1]
                resLen = r + 1 - l
            l -= 1
            r += 1
        return res, resLen
