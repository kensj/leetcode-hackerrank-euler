class Solution:
    def maxProfit(self, prices):
        profit = 0
        minprice = -1
        for x in range(0, len(prices)):
            if minprice == -1 or prices[x] < minprice: minprice = prices[x]
            elif prices[x] - minprice > profit: profit = prices[x]-minprice
        return profit