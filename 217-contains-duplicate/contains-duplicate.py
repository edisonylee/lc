from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hasDuplicates = False
        seen = defaultdict(int)
        for num in nums:
            if num in seen:
                hasDuplicates = True
            seen[num] = 1
        return hasDuplicates
        