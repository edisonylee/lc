class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Given a 1-indexes array of integers numbers that is already sorted
        # in non-decreasing order, find 2 numbers such that they up to a specific target number
        # sorted already, non-decreasing order,
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum < target: # [2,7,11,15] increase sum by increasing i
                i += 1
            elif  sum > target: # decrease sum
                j -= 1    
        return []