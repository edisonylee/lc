class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums) # init
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            ans[i] = prefix # 1, 3, 6, 10
        return ans