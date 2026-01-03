class Solution:
    def countElements(self, arr: List[int]) -> int:
        # Given an array, count how many elements x there are, such that x + 1 is also in arr,
        # If there are duplicates in arr, count them separately
        deezNuts = set(arr)
        elements = 0
        for num in arr:
            plusOne = num + 1
            if plusOne in deezNuts:
                elements += 1
        return elements