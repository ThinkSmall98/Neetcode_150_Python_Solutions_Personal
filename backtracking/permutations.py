# Time: O(∑ N, k=1, P(N,k)) were P(N, k) = N!/(N-k)!
# Space: O(N!) Keep N! solutions
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(first):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        backtrack(0)
        return res
        
        
