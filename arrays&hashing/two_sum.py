class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in count_dict:
                return [i, count_dict[complement]]
            count_dict[nums[i]] = i
'''
Use dict, find if complement exists
'''
