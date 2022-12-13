# Time: O(n)
# Space: O(1)

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matched_indices = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            for i, val in enumerate(triplet):
                if val == target[i]:
                    matched_indices.add(i)
        return len(matched_indices) == 3 # check that all values of target can be matched
            

# First ignore all triplets with values greater than the target triplet values
# Then go thru remaining triplets and see if any have the target triplet values
