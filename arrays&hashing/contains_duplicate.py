# Method 1: Naive
# Time: O(n^2)
# Space: O(1)
def containsDuplicate(self, nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] == nums[j]:
                return True
    return False
  
# Method 2: Hashset
# Time: O(n)
# Space: O(n)
def containsDuplicate(self, nums: List[int]) -> bool:
    unique_nums = set()
    for num in nums:
        if num not in unique_nums:
            unique_nums.add(num)
        else:
            return True
    return False
  
# Method 3: Sorting
# Time: O(n logn)
# Space: O(1)
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums) - 1): # off by 1 error
        if nums[i] == nums[i + 1]:
            return True
    return False
