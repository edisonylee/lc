class Solution: #brute force
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)): #first loop iterates through i
            for j in range(i+1, len(nums)): #second loop iterates compares the value at i and searches through the rest of the list
                if nums[i]==nums[j]: #compare condition
                    return True #return true
        return False #return false
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #creates hash set
        for num in nums: #for each value of num in nums
            if num in seen: #if num is in the set
                return True #return true
            seen.add(num) #if not in the set add it and return false
        return False
