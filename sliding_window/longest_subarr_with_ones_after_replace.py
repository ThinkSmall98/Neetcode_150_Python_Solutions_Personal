class Solution:
    def findLength(self, arr, k):
      i = ones_count = 0
      for j in range(len(arr)):
        if arr[j] == 1:
          ones_count += 1
        if (j - i + 1) - ones_count > k:
          if arr[i] == 1:
            ones_count -= 1
          i += 1
        
      return j - i + 1
'''
Can only replace 0s with 1s. Must have all ones in array at end
'''
