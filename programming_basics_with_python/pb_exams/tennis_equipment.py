import math

rocket_price = float(input())
rockets_count = int(input())
shoes = int(input())

all_rockets_price = rocket_price * rockets_count
one_pair_shoes = rocket_price / 6
all_shoes_price = one_pair_shoes * shoes
other_things = (all_rockets_price + all_shoes_price) * 0.2
total = all_rockets_price + all_shoes_price + other_things

price_djokovic = math.floor(total / 8)
price_sponsors = math.ceil(total * 7 / 8)

print(f"Price to be paid by Djokovic {price_djokovic}")
print(f"Price to be paid by sponsors {price_sponsors}")
