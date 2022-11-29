# Time: O(n * sum(nums)). Target = sum(nums)/2. n = len(nums)
# Space: O(sum(nums)). Set limited by target.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: # odd sum
            return False 
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for n in dp:
                if n + nums[i] == target:
                    return True
                nextDP.add(n + nums[i])
                nextDP.add(n)
            dp.update(nextDP)
        return False
