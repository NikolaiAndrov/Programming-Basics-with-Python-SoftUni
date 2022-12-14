over_20kg_price = float(input())
bags_weight = float(input())
days_left = int(input())
bags_count = int(input())

current_price = 0

if bags_weight < 10:
    current_price = over_20kg_price * 0.2
elif 10 <= bags_weight <= 20:
    current_price = over_20kg_price * 0.5
else:
    current_price = over_20kg_price

if days_left < 7:
    current_price *= 1.4
elif 7 <= days_left <= 30:
    current_price *= 1.15
else:
    current_price *= 1.1

current_price *= bags_count

print(f"The total price of bags is: {current_price:.2f} lv.")