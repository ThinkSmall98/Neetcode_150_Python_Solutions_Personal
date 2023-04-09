from collections import Counter
from heapq import nlargest
class Solution:
    # Counter + most_common
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [key for key, val in Counter(nums).most_common(k)]
        return res
          
    # bucket sort
    # Time: O(n) where n = len(nums)
    # Space: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_arr = [[] for _ in range(len(nums) + 1)]
        count_num = Counter(nums)

        for num, freq in count_num.items():
            freq_arr[freq].append(num)
        res = []
        for i in range(len(freq_arr) - 1, -1, -1):
            for num in freq_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
