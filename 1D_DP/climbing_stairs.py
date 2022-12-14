# Time complexity : O(n). Single loop up to n is required to calculate nth fibonacci number.
# Space complexity : O(1). Constant space is used.

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            two, one = two + one, two
        return two

# Fibonnaci numbers
