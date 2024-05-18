# Time: O(n * 4^n), Space: O(n) where n = len(digits)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []

        numToChar = {2: 'abc', 3: 'def', 4: 'ghi',
                    5:'jkl', 6: 'mno', 7: 'pqrs', 
                    8: 'tuv', 9: 'wxyz'}

        def dfs(i):
            if i == len(digits):
                res.append(''.join(path))
                return
            for char in numToChar[int(digits[i])]:
                path.append(char)
                dfs(i + 1)
                path.pop()

        if digits:
            dfs(0)

        return res
