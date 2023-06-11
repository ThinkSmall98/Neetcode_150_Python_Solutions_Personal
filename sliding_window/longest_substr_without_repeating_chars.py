class Solution:
    # Time: O(2n) = O(n)
    # Space: O(1)
    # def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)
        return res
# reset set if there are repeating characters

    # Time: O(2n) = O(n)
    # Space: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        map_dict = {}
        left = 0
        for right in range(len(s)):
            if s[right] in map_dict:
                left = max(left, map_dict[s[right]] + 1) # skip to after where duplicate letter was first seen
            res = max(res, right - left + 1)
            map_dict[s[right]] = right
        return res

