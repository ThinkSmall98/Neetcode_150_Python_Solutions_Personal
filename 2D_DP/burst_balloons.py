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

    # cache using dict
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]

        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    coins = nums[left] * nums[pivot] * nums[right]
                    coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                    cache[(left, right)] = max(coins, cache.get((left, right), 0))
        return cache.get((0, len(nums) - 1), 0)
