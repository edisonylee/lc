class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given an array nums, and int target, return indices of the two numbers such that they add up to target,
        # you may assume that each input would have exactly ONE solution, and you may not use the same element twice.
        dic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic:
                return [i, dic[complement]]
            dic[nums[i]] = i