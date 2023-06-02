class Solution:
    # Time: O(n)
    # Space: O(1)
    def twoSum(self, nums: List[int], i: int, target: int) -> int:
        left, right = i + 1, len(nums) - 1
        res = 0
        while left < right:
            sum_nums = nums[left] + nums[right] + nums[i]
            if sum_nums < target:
                res += right - left
                left += 1
            else:
                right -= 1
        return res

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0 # indices
        nums.sort()
        for i in range(len(nums) - 2): # -2 bc there aren't enough numbers left after
            res += self.twoSum(nums, i, target)
        return res
