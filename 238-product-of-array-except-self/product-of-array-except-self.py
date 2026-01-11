from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        For each index i, return the product of all elements in nums
        except nums[i], without using division.

        Strategy:
        - First pass builds prefix products (everything to the left of i)
        - Second pass builds postfix products (everything to the right of i)
        - Multiply prefix * postfix to get the final answer for each index
        """

        # Initialize result array where res[i] will eventually hold
        # (product of elements to the left of i) * (product of elements to the right of i)
        res = [1] * len(nums)

        # prefix holds the product of all elements BEFORE index i
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix            # store product of left side
            prefix *= nums[i]          # update prefix to include nums[i]

        # postfix holds the product of all elements AFTER index i
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix          # multiply by product of right side
            postfix *= nums[i]         # update postfix to include nums[i]

        return res
