class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        mini=prices[0]
        for i in range(len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            if prices[i]>mini and prices[i]-mini>profit:
                profit=prices[i]-mini
        return profit
