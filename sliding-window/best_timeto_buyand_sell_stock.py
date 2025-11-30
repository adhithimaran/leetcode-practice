
def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)):
        print(f'this is i: {prices[i]}')
        for j in range(i+1, len(prices)):
            print(f'this is j: {prices[j]}')
            prof = prices[j] - prices[i]
            print(f'Pofit: {prof}')
            if (prof > max_profit):
                max_profit = prof
    return max_profit


prices = [10,1,5,6,7,1]
prices2 = [10,8,7,5,2]
print(maxProfit(prices2))