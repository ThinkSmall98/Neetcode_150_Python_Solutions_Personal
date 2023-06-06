class Solution:
    # Time: O(n)
    # Space: O(1)
    def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                volume += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                volume += max_right - height[right]
        return volume


# get local max
