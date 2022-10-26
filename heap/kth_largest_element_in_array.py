# from heapq import heapify, heappop, heappush
# # Time: O(nlogk), Space: O(k)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums_rev = [-1*i for i in nums]
#         heapify(nums_rev)
#         res = 0
#         while k > 0:
#             res = heappop(nums_rev)
#             k -= 1
#         return res * -1
        
# Time: O(n) avg, O(n^2) worst, Space: O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = len(nums) - k
        
        def quickSelect(l, r):
            pivot, pointer = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            nums[pointer], nums[r] = nums[r], nums[pointer]
            
            if pointer > index: return quickSelect(l, pointer - 1)
            elif pointer < index: return quickSelect(pointer + 1, r)
            else: return nums[pointer]
        return quickSelect(0, len(nums) - 1)
               
