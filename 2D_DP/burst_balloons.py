from functools import lru_cache
# Time: O(n^3)
# Space: O(n^2) bc n^2 subproblems
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @lru_cache(None) # memoization
        def dp(l, r):
            if r - l < 0:
                return 0
            res = 0 
            for i in range(l, r + 1):
                gain = nums[l - 1] * nums[i] * nums[r + 1] # if we pop this last
                remain = dp(l, i - 1) + dp(i + 1, r)
                res = max(res, gain + remain)
            return res
        return dp(1, len(nums) - 2)
