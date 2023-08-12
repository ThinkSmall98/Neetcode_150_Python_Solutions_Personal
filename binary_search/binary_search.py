class Solution:
    # Time: O(log(n))
    # Space: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2) # add left to make sure there's no overflow
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else: # target > nums[mid]
                left = mid + 1
        return -1
