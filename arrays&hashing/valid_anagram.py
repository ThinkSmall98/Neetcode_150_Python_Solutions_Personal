# Method 1: Counter
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count
    
# Method 2: defaultdict
from collections import defaultdict
class Solution:
    # Time: O(n)
    # Space: O(26) = O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = defaultdict(int)
        for s_char in s:
            s_dict[s_char] += 1

        t_dict = defaultdict(int)
        for t_char in t:
            t_dict[t_char] += 1
        
        return s_dict == t_dict
# Method 3: Sorting
class Solution:
    # Time: O(n logn)
    # Space: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
