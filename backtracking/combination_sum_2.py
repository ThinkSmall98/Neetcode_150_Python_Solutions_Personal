# Time: O(2^n), Space: O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
    
        def dfs(i, remaining):
            if remaining == 0:
                res.append(subset.copy())
                return
            if remaining < 0 or i == len(candidates):
                return
            # add candidates[i]
            subset.append(candidates[i])
            dfs(i + 1, remaining - candidates[i])
            # remove candidates[i]
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
                if remaining < candidates[i]:
                    break
            dfs(i + 1, remaining)
        dfs(0, target)
        return res







        # res = []
        # candidates.sort()
        # len_candidates = len(candidates)

        # def dfs(start_i, arr, remaining):
        #     if remaining == 0:
        #         res.append(arr.copy())
        #         return
        #     if remaining < 0:
        #         return

        #     prev = -1
        #     for i in range(start_i, len_candidates):
        #         if prev == candidates[i]:
        #             continue
        #         if remaining < candidates[i]:
        #             break
        #         arr.append(candidates[i])
        #         dfs(i + 1, arr, remaining - candidates[i])
        #         arr.pop()
        #         prev = candidates[i]

        # dfs(0, [], target)
        # return res



