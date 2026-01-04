class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Given an array with prices
        # Return max profit - highest prices in the week - lowest price in the week in order
        # [ 7, 1, 5, 3, 6, 4]
        #  I want to find the lowest price of the week, loop until len - 1
        # I want to find the highest price of the week, loop until len
        ans = 0
        left = 0
        for right in range(1, len(prices)): # looping through to find the buy day
            if prices[right] < prices[left]: # don't consider last element as a 
                left = right # if right is lower than swap
            elif prices[right] > prices[left]:
                ans = max(ans, prices[right] - prices[left])
        return ans
                

