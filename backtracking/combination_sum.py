# N = num of candidates, T = target value, M = min. val among candidates
# Time: O(N^(T/M + 1)). Fan-out of each node bounded to N & max depth of tree is T/M
# Space: O(T/M)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or target < total:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res
        
