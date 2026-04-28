class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # track lowest and store profit
        low = 0
        profit = 0

        for i in range (0, len(prices)):
            if i == 0:
                # if first day, automatically lowest so far
                low = prices[i]
            elif prices[i] < low:
                # if new price is lower, reset low
                low = prices[i]
            elif prices[i] > low:
                # if new price is higher than low, calc profit and see if its the largest
                newProfit = prices[i] - low
                if newProfit > profit:
                    profit = newProfit

        return profit

        