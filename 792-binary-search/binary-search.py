class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 # init left pointer
        right = len(nums) - 1 # init right pointer
        while left <= right: # before they meet in the middle
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1