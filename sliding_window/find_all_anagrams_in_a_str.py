from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n1, n2 = len(p), len(s)
        p_dict = Counter(p)
        s_dict = Counter(s[:n1])
        if p_dict - s_dict == {}:
            res.append(0)
        for i in range(n1, n2):
            s_dict[s[i - n1]] -= 1
            s_dict[s[i]] += 1
            if p_dict - s_dict == {}:
                res.append(i - n1 + 1) # add 1 to get value after i
        return res
