# Time: O(n)
# Space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= pos:
                pos = i
        return pos == 0

# go backwards
