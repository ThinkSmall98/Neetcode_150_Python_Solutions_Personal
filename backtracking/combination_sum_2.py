# Time: O(2^n), Space: O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(pos, arr, remaining):
            if remaining == 0:
                res.append(arr.copy())
                return
            if remaining <= 0:
                return
            # keep track of prev num
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                # If candidates[i] > target it will never be a valid combo
                if remaining < candidates[i]:
                    break
                arr.append(candidates[i])
                dfs(i + 1, arr, remaining - candidates[i])
                arr.pop()
                prev = candidates[i]

        dfs(0, [], target)
        return res


