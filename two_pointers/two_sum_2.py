class Solution:
    # Time: O(n)
    # Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_num = numbers[left] + numbers[right]
            if sum_num == target:
                return [left + 1, right + 1]
            elif sum_num < target:
                left += 1
            else: # sum_num > target
                right -= 1
