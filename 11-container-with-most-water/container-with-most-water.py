class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0 # set var
        left, right = 0, len(height) - 1
        while left < right:
            curr_height = min(height[left], height[right])
            curr_width = right - left
            curr_area = curr_height * curr_width
            max_water = max(max_water, curr_area)
            # Move the pointer at the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
