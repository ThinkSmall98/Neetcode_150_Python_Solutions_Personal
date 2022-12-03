class Solution:
    # 1D dp
    # Time: O(t * n) where t = sum(nums) & n = len(nums)
    # Space: O(t)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        dp = [0] * (2 * total + 1) # keep track neg. & pos.
        dp[nums[0] + total] = 1
        dp[-nums[0] + total] += 1

        for i in range(1, len(nums)):
            next = [0] * (2 * total + 1)
            for s in range(-total, total + 1):
                if dp[s + total] > 0:
                    next[s + nums[i] + total] += dp[s + total]
                    next[s - nums[i] + total] += dp[s + total]
            dp = next
        return dp[target + total] if abs(target) <= total else 0


      # Memoization
      # Time: O(t * n) where t = sum(nums) & n = len(nums)
      # Space: O(t * n)
      # dp = {} # (index, total) -> # of ways
      
      def backtrack(i, total):
          if i == len(nums):
              return 1 if total == target else 0
          if (i, total) in dp:
              return dp[(i, total)]
          dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                           backtrack(i + 1, total - nums[i]))
          return dp[(i, total)]
      return backtrack(0, 0)
