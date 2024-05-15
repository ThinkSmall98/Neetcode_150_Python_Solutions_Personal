# N = num of candidates, T = target value, M = min. val among candidates
# Time: O(N^(T/M + 1)). Fan-out of each node bounded to N & max depth of tree is T/M
# Space: O(T/M)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, arr, curr_sum):
            if curr_sum == target:
                # append shallow copy of arr bc of recursion
                res.append(arr.copy())
                return 
            if curr_sum > target or i == len(candidates):
                return
            # add candidates[i]
            arr.append(candidates[i])
            dfs(i, arr, curr_sum + candidates[i])
            # pop candidates[i]
            arr.pop()
            dfs(i + 1, arr, curr_sum)
        dfs(0, [], 0)
        return res
        
