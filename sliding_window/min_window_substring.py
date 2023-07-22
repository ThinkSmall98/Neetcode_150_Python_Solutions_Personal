from collections import Counter
class Solution:
    # Time: O(len(t) + len(s))
    # Space: O(len(t) + len(s))
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        interval = [-1, -1]
        min_len = float('inf')
        have, need = 0, len(count_t)
        left = 0
        count_s = {}
        for right in range(len(s)):
            count_s[s[right]] = 1 + count_s.get(s[right], 0)

            if count_s[s[right]] == count_t.get(s[right], 0):
                have += 1

            while have == need:
                if right - left + 1 < min_len:
                    interval = [left, right]
                    min_len = right - left + 1
                count_s[s[left]] -= 1
                
                if count_s[s[left]] < count_t.get(s[left], 0):
                    have -= 1
                left += 1
        
        left, right = interval
        return s[left:right + 1] if min_len !=  float('inf') else ''

# check that keys exist first
