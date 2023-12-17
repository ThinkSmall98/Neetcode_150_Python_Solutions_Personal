class Solution:
    # Time: O(n)
    # Space: O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_freq = max(max_freq, count[s[right]])

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
        return (right - left + 1)
'''
Don't actually need res bc the sliding window will always adjust to be the max len of longest substr
We only move to the right once each time
'''
