from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums):
        hSet = defaultdict(int)
        for num in nums:
            hSet[num] += 1

        ans = -1
        for num, count in hSet.items():
            if count == 1:
                ans = max(ans, num)

        return ans