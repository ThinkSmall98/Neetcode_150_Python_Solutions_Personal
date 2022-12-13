# Time: O(n) where n = len(s)
# Space: O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = leftMax = 0
        for char in s:
            leftMin -= 1 if char != "(" else -1
            leftMax += 1 if char != ")" else -1
            # if char == "(":
            #     leftMin += 1
            #     leftMax += 1
            # elif char == ")":
            #     leftMin -= 1
            #     leftMax -= 1
            # else: # *
            #     leftMin -= 1
            #     leftMax += 1
            if leftMax < 0:
                return False
            leftMin = max(leftMin, 0)
        return leftMin == 0

# keep track of range of open left brackets after processing each char in s
