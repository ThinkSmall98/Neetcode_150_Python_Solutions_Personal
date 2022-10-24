from heapq import heapify, heappop, heappush

# Time: O(N log(N)), Space: O(N)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_arr = [-1 * i for i in stones]
        heapify(stones_arr)
        
        while len(stones_arr) > 1:
            stone_1 = heappop(stones_arr)
            stone_2 = heappop(stones_arr)
            if stone_1 != stone_2:
                heappush(stones_arr, stone_1 - stone_2)
        return -heappop(stones_arr) if stones_arr else 0
