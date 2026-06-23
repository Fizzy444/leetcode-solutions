class Solution(object):
    def maxProfit(self, prices):
        mi = prices[0]
        profit = 0
        for p in prices:
            if p < mi:
                mi = p
            elif p - mi > profit:
                profit = p - mi
        return profit