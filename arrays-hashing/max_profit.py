def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    i, j = 0, 1

    while i < len(prices) - 1:
        buy = prices[i]
        sell = prices[j]
        curr_profit = sell - buy
        if (curr_profit >= 0):
            max_profit = max(curr_profit, max_profit)

        j += 1
        if j == len(prices):
            i += 1
            j = i + 1
    return max_profit