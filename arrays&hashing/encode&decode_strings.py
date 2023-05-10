class Codec:
    # Time: O(n)
    # Space: O(1)
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for string in strs:
            str_len = len(string)
            if str_len < 10:
                str_len = '00' + str(str_len)
            elif str_len < 100:
                str_len = '0' + str(str_len)
            else:
                str_len = str(str_len)
            res += str_len + string
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            length = int(s[i:i + 3])
            word = s[i + 3: i + 3 + length]
            res.append(word)
            i += 3 + length
        return res
