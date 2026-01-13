class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 1. Sort in-place (don't assign to a variable)
        ans = []
        n = len(nums)
        
        for i in range(n - 2):
            # 2. Skip duplicates for the fixed number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 3. Initialize two pointers: left (j) and right (k)
            j = i + 1
            k = n - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    # 4. Skip duplicates for j and k to ensure distinct triplets
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    # Move both pointers inward after finding a match
                    j += 1
                    k -= 1
                    
                elif curr_sum < 0:
                    # Sum is too small, move left pointer to the right to increase sum
                    j += 1
                else:
                    # Sum is too big, move right pointer to the left to decrease sum
                    k -= 1
                    
        return ans