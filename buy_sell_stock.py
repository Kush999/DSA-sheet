#Best Time to Buy and Sell Stock

def maxProfit(prices,n):
    diff = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if prices[j]>prices[i] and prices[j]-prices[i]>diff:
                diff = prices[j]-prices[i]
    return diff

prices=[7,1,5,3,6,4]
n=len(prices)
print(maxProfit(prices,n))