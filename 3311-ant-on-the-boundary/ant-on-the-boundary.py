class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        runningTotal = 0
        ans = 0
        for i in range(len(nums)): # 2,3,-5
            runningTotal += nums[i] # Call 1: 2+3-5
            if runningTotal == 0:
                ans += 1
        return ans


            
            