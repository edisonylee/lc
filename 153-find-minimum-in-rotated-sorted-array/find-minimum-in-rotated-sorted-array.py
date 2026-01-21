class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 # initialize pointers
        right = len(nums) - 1
        
        while left < right: # while left is less than the right
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1 # [1,2,3,4,5]
            else:
                right = mid
        return nums[left]