# Time: O(2^n), Space: O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(comb, remain, pos):
            if remain == 0:
                res.append(comb[:]) # return shallow copy
                return
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                if remain < candidates[i]: # optimize by stopping when exceeding remaining val
                    break
                comb.append(candidates[i])
                backtrack(comb, remain - candidates[i], i + 1)
                comb.pop()
        backtrack([], target, 0)
        return res
