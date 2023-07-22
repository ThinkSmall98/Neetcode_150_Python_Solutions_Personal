from collections import Counter
class Solution:
    # Time: O(len(t) + len(s))
    # Space: O(len(t) + len(s))
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        res = [-1, -1]
        min_len = float('inf')
        have, need = 0, len(count_t)
        l = 0
        window = {}
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                have += 1
            while have == need:
                # update result
                if (r - l + 1) < min_len:
                    res = [l, r]
                    min_len = r - l + 1
                # pop from left of our window
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if min_len != float('inf') else ''
