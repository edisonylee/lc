class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        array_length = m * n - 1

        left = 0
        right = array_length
        while left <= right:
            mid = (left+right) // 2
            row = mid // n
            col = mid % n
            value = matrix[row][col]
            if value == target:
                return True
            if value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
