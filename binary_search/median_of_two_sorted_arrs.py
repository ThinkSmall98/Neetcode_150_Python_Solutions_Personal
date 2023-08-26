class Solution:
    # Time: O(log(min(m, n)))
    # Space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(nums1), len(nums2)

        if n < m:
            return self.findMedianSortedArrays(nums2, nums1) # switch so nums1 is smaller
            
        l, r = 0, m
        while l <= r: 
            i = l + ((r - l) // 2) # A
            j = (m + n + 1)// 2 - i  # + 1 bc we want to account for odd & even number of elements

            A_left = float("-inf") if i == 0 else A[i-1]
            A_right = float("inf") if i == m else A[i]
            B_left = float("-inf") if j == 0 else B[j-1]
            B_right = float("inf") if j == n else B[j]

            # if partition is right, left values of A & B <= right values of B & A
            if A_left <= B_right and B_left <= A_right:
                # even
                if (m + n) % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                # odd
                else: 
                    return max(A_left, B_left)
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
