class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Given nums, return T if num appears more than once, F is every element distinct
        # Initial thoughts: I want to loop through nums.
        # Then, I want to check to see if it's in the set, and if it is not in the set Im going to add it to the set.
        # Then we can return True if it's in the set, False otherwise.
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False