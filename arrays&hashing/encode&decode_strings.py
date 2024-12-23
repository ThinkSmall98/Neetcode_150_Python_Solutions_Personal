class Solution:
    # Put number and then _ after to represent length of each word
    # Time: O(n) where n = len(strs)
    # Space: O(1)
    def encode(self, strs: List[str]) -> str:
        s = ''
        for string in strs:
            len_string = len(string)
            s += f'{len_string}_{string}'
        return s

    # Time: O(m) where m = sum(len of all strs)
    # Space: O(1) (don't count res in space complexity)
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i + 1
            while s[j] != '_': # need to see if strs[i] is 2 or 3
                j += 1
            len_string = int(s[i: j])
            j += 1 # move 
            res.append(s[j: j + len_string])
            i = j + len_string
        return res
