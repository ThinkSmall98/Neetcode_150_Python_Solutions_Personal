class Solution:
  def findLength(self, str1, k):
      i = 0
      uniq_chars = {}
      for j in range(len(str1)):
        uniq_chars[str1[j]] = 1 + uniq_chars.get(str1[j], 0)
        if len(uniq_chars) > k:
          uniq_chars[str1[i]] -= 1
          if uniq_chars[str1[i]] == 0:
            del uniq_chars[str1[i]]
          i += 1
      return j - i + 1

'''
For sliding window, don't need to keep decreaesing the window.
Just decrease it once and then move on. 
j - i + 1 will be the max len regardless.

'''
