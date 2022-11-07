# Time: O(n * 4^n), Space: O(n) where n = len(digits)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        numToChar = {"2":"abc", "3":"def","4": "ghi", "5": "jkl",
                    "6": "mno", "7": 'pqrs', '8': 'tuv', '9':'wxyz'}
        def backtrack(i, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            for c in numToChar[digits[i]]:
                path.append(c)
                backtrack(i + 1, path)
                path.pop()
        if digits:
            backtrack(0, [])
        return res
