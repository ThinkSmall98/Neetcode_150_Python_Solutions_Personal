# Time: O(n^2)
# Space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            res += self.countPali(s, l, r)

            # even
            l, r = i, i + 1
            res += self.countPali(s, l, r)
        return res

    def countPali(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
