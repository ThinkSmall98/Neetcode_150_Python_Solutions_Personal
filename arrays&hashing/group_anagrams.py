from collections import defaultdict
class Solution(object):
    # Time: O(n*k log k), n = len(strs), k = max(len(a str in strs))
    # Space: O(n * k)
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
      
      
    # Time: O(n*k), n = len(strs), k = max(len(a str in strs))
    # Space: O(n)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(word)
        return res.values()
