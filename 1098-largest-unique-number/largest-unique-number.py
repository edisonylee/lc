from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
    # Create a HashMap with all of the counts of all of the elements
        # Iterate over nums, and assign key, value pairs to the HashMap
    # Sort numbers lowest to highest, loop starting from the end of the sorted list
        # If the value == 1
            # We can return the key
        # Return -1
        hSet = defaultdict(int) # Create the HSet
        for num in nums: # Loop through the array
            hSet[num] += 1 # Counting frequency of num
        for countedElement in sorted(hSet.keys(), reverse = True): # Loop through the counted elements
            if hSet[countedElement] == 1:
                return countedElement
        return -1
        
    
    