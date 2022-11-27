# Time: O(n)
# Space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for n in nums:
            curMax, curMin = max(n * curMax, n * curMin, n), min(n * curMax, n * curMin, n)
            res = max(res, curMax)
        return res
