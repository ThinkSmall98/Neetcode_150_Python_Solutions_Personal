# Time: O(n * log(n)). heapify = n. heappop = log(n) 
# Space: O(n) where n = len(hand)
from heapq import heapify, heappop
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        minH = list(count.keys())
        heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count: # make sure i exists in count
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]: # makes sure only min value has 0 occurences left to use
                        return False
                    heappop(minH)
        return True
