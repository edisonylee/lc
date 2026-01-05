class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Make a set 
        count = 0
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        