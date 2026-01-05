class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hasDuplicates = False
        seen = {}
        for num in nums:
            if num in seen:
                hasDuplicates = True
            if num not in seen:
                seen[num] = 0
        return hasDuplicates
        