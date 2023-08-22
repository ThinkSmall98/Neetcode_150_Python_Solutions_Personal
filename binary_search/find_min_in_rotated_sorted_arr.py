class Solution:
    # Time: O(log(n))
    # Space: O(1)
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            m = l + ((r - l) // 2)
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res
        
# Brute force: go thru array and keep track of lowest value
# Array is sorted, which is a clue that we should use binary search
