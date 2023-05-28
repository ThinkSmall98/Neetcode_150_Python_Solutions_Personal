class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    
    # Time: O(n)
    # Space: O(n)
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        return s == s[::-1]
