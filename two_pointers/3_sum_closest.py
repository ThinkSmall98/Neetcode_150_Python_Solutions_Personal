class Solution:
    # Time: O(n)
    # Space: O(1)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_nums = nums[i] + nums[left] + nums[right]
                if abs(sum_nums - target) < abs(diff):
                    diff = sum_nums - target # don't do abs bc we need real sum to be returned
                if sum_nums < target:
                    left += 1
                elif sum_nums == target:
                    return target
                else:
                    right -= 1
            if diff == 0:
                break
        return target + diff
# get difference of sum_nums + target. Keep track of smallest difference. 
