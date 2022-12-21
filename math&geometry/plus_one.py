# Time: O(n) where n = len(digits)
# Space: O(n) bc we have to go over entire arr before appending
# Whenever the combined size of elements of that list exceeds the memory space of the original list, it acquires the contiguous memory at another location of size double its previous size.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            digits[i] = 0
        return [1] + digits
