from collections import deque
class Solution:
    # Time: O(n)
    # Space: O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []
        left = right = 0

        for right in range(len(nums)):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[right]:
                q.pop()
                
            q.append(right)

            # remove left val from window
            if left > q[0]:
                q.popleft()

            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1

        return output

# Brute force: iterate over all windows & then iterate thru all elements in a window
