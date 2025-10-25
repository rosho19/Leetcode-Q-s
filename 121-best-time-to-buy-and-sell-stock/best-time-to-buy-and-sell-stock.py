class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1 # set up two pointers to iterate through the list with a price we buy and sell 
        maxprof = 0 # variable to store the maxprofit so far

        while sell < len(prices): # run the loop until the sell variable reaches the end, since we have to sell before the list ends or we don't buy at all
            if prices[buy] < prices[sell]: # if the profit is positive, it's possible it could be higher than the previous max profit
                profit = prices[sell] - prices[buy]
                maxprof = max(maxprof, profit)
            else: # if the profit isn't positive, then we know that the current value of the sell pointer is lower, so it presents a better buying opportunity
                buy = sell
            sell += 1 # continuously increment the sell pointer to find better opportunities
        return maxprof