# Time: O(∑ N, k=1, P(N,k)) were P(N, k) = N!/(N-k)!
# Space: O(N!) Keep N! solutions
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            for num in nums:
                if num not in arr:
                    arr.append(num)
                    dfs(arr)
                    arr.pop()
                    # don't need to do dfs again bc we have to keep a certain num of elements in arr
        dfs([])
        return res
        
