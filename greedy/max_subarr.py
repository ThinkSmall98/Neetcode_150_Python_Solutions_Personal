# Time: O(n)
# Space: O(1). Only use 2 vars
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarr = cur_subarr = nums[0]

        for num in nums[1:]:
            cur_subarr = max(num, num + cur_subarr)
            max_subarr = max(max_subarr, cur_subarr)
        return max_subarr
