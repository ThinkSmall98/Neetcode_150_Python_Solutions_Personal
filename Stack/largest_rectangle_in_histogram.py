class Solution:
    # Time: O(n)
    # Space: O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        # could still be values left in stack even when pointer is at the end
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area
