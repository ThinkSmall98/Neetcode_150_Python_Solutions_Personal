class Solution:
    # Time: O(log(n))
    # Space: O(1)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            # left subarray
            elif nums[l] <= nums[m]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right subarray
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else: 
                    r = m - 1

        return -1
