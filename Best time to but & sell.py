# Best time to buy and sell:

def maxprofit(l):
    max_profit=0
    buy=l[0]

    for price in l:
        if price>buy:
            max_profit=max(max_profit, price-buy)
        else:
            buy=price
  
    return max_profit

    
l = [7,1,5,3,6,4]
print(maxprofit(l))
