# Time: O(n) where n = len(s)
# Space: O(1). Actually O(26)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {char: i for i, char in enumerate(s)} # stores last index for each unique char
        size = end = 0
        res = []
        for i, char in enumerate(s):
            size += 1
            end = max(end, lastIndex[char])
            if end == i: # reached end of one partition
                res.append(size)
                size = 0
        return res


# HashMap mapping char: LastIndex
