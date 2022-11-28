# Binary search solution
# Time: O(n * log(n))
# Space: O(n)
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num) # returns left-most index to insert given element, maintaining sorted order
            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num # replace the first element in sub greater than or equal to num
        return len(sub)
        
# DP Solution
# Time: O(n^2)
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
