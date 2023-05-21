class Solution:
    # Time: O(n)
    # Space: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if (num - 1) not in nums_set:
                longest = 1
                while num + longest in nums_set:
                    longest += 1
                res = max(longest, res)
        return res
