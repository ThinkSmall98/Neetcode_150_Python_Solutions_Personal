# Time: O(n)
# Space: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        downOne, downTwo = 0, 0

        for i in range(2, len(cost) + 1):
            downOne, downTwo = min(downOne + cost[i - 1], downTwo + cost[i - 2]), downOne
        return downOne


# Top floor is beyond the last value of array
# recurrence relation depends only on prev. 2 approaches
# Bottom-up DP approach

# Initialize two vars: downOne & downTwo that represent min cosot to reach 1 and 2 steps below current step

        
