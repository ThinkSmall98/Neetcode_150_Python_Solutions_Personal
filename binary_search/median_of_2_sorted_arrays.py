class Solution:
    # Time: O(log(min(m, n)))
    # Space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            i = l + ((r - l) // 2) # A
            j = half - i - 2 # B (subtract 2 bc arrs are indexed at 0)

            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i + 1] if i < len(A) - 1 else float("inf")
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if j < len(B) - 1 else float("inf")

            # partition is correct
            if A_left <= B_right and B_left <= A_right:
                # odd
                if total % 2:
                    return min(A_right, B_right)
                # even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
