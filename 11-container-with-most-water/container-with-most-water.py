class Solution:
    def maxArea(self, height: List[int]) -> int:
        # You are given an array height of n length
        left = 0
        right = len(height) - 1
        maximum_water = 0

        while left < right:
            min_height = min(height[left], height[right]) # Find the smaller height
            curr_width = right - left # find the current width
            curr_area = curr_width * min_height # current area calculation
            maximum_water = max(maximum_water, curr_area)
            
            if height[left] > height[right]: #keep the bigger value
                right -= 1
            else:
                left += 1
        return maximum_water

