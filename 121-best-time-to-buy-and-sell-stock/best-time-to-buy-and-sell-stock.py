class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # You are given an integer array prices where
        # prices [i] is the price of NeetCoin on the ith day. 
        # You may choose a single day to buy one NeetCoin and choose a different day in the fu ture to sell ti.
        # Return the maximum profit you can achieve. You may choose to not make any transacations.

        profit = 0 # init profit
        left = 0 # init left pointer
        for right in range(1, len(prices)): # loop thru starting from index 1 bc left is at index 0
            if prices[right] < prices[left]: # so the min(left) is going to be swapped until last element
                left = right
            elif prices[right] > prices[left]: # prices[right] greater than prices[left] means that we can subtract to find the profit
                profit = max(profit, prices[right] - prices[left]) # the profit is going to be recalculated for each pass
        
        # [10, 1, 5, 6, 7, 1]
        # 1. 1 < 10 so now left = 1. Now, for index 2, 5 is not less so lets calculate 5 - 1. It's 4, 5, 6. Then 
        # for the last element left pointer is sewt to the right but nothing else is ran so it doesnt really matter.
        return profit