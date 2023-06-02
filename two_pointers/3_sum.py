class Solution:
    def twoSum(self, nums: List[int], i: int, res: List[List[int]]) -> List[List[int]]:
        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = nums[left] + nums[right] + nums[i]
            if three_sum < 0:
                left += 1
            elif three_sum > 0:
                right -= 1
            else:
                res.append([nums[left], nums[right], nums[i]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # while left < right and nums[right] == nums[right + 1]:
                #     right -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: # all numbers after cannot sum to 0 bc they're bigger
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res



# Take number that is not positive (<= 0), because if it's positive all nums will be greater than that
