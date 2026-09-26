class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        j = 0
        for i in range(1, len(prices)):
            if prices[j] < min_buy:
                min_buy = prices[j]
            curr_profit = prices[i] - min_buy
            if curr_profit > max_profit:
                max_profit = curr_profit
            j += 1

        return max_profit

           
            