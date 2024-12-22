from collections import Counter, defaultdict
class Solution(object):
    # Time: O(n*k log k), n = len(strs), k = max(len(a str in strs))
    # Space: O(n * k)
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
      
    # Time: O(m * n) where m = len(strs) & n = len(longest string in strs)
    # Space: O(m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            # instead of using Counter can just keep array of len(26)
            count = [0] * 26
            for char in string:
                # subtract ord(char) by ord(a)
                count[ord(char) - ord('a')] += 1 
            res[tuple(count)].append(string)
        return res.values()
        
    # 2 arrays
    # Time: O(m * n) where m = len(strs) & n = len(longest string in strs)
    # Space: O(m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = []
        groups = []
        for string in strs:
            count_dict = Counter(string)
            if count_dict not in seen:
                seen.append(count_dict)
                
                groups.append([string])
            else:
                # get index of it in list and append it to that array
                groups[seen.index(count_dict)].append(string)
        return groups

'''
{a: 1, c: 2, t: 1}
'''
