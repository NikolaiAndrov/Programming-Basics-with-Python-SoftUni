rent = float(input())

cake_price = rent * 0.2
drinks_price = cake_price * 0.55
animator = rent / 3
budget = rent + cake_price + drinks_price +animator

print(budget)