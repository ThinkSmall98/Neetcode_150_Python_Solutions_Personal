class Solution:
    # Time: O(len(s1) + (len(s2) - len(s1)) * len(s1))
    # Space: O(len(s1))
    def checkInclusion(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        s1_count = Counter(s1)
        
        for i in range(0, n2 - n1 + 1):
            s2_count = Counter(s2[i: n1 + i])
            if s2_count == s1_count:
                return True
        return False
        
    # Time: O(len(s1) + len(s2 - s1))
    # Space: O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # want to make sure s2 is longer than s1
        if len(s2) < len(s1):
            return False
        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1 

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            index = ord(s2[right]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            left += 1
            
        return matches == 26
