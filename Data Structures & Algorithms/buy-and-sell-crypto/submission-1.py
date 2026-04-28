class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        profit = 0

        for i in range (0, len(prices)):
            if i == 0:
                low = prices[i]
            elif prices[i] < low and i < len(prices)-1:
                low = prices[i]
            elif prices[i] > low:
                newProfit = prices[i] - low
                if newProfit > profit:
                    profit = newProfit

        return profit

        