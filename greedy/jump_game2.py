# Time: O(n)
# Space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        res = 0 
        while r < len(nums) - 1:
            max_pos = 0
            for i in range(l, r + 1):
                max_pos = max(max_pos, i + nums[i])
            l = r + 1
            r = max_pos
            res += 1
        return res

# use 2 pointers (window). Simplified BFS.
# i + nums[i]: curr position + fartherest we can jump to
