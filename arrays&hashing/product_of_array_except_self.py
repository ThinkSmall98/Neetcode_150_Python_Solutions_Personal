class Solution:
    # Time: O(n)
    # Space: O(n) 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [0] * length
        right = [0] * length
        res = [0] * length
        left[0] = 1
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]

        right[length - 1] = 1
        for j in range(length - 2, -1, -1):
            right[j] = nums[j + 1] * right[j + 1]
        for k in range(length):
            res[k] = left[k] * right[k]
            
        return res
      
class Solution:
  # Time: O(n)
  # Space: O(1) bc output array doesn't count
  def productExceptSelf(self, nums: List[int]) -> List[int]:
      length = len(nums)
      res = [0] * length
      res[0] = 1
      for i in range(1, length):
          res[i] = nums[i - 1] * res[i - 1]

      right = 1
      for j in range(length - 1, -1, -1):
          res[j] *= right
          right *= nums[j]

      return res
