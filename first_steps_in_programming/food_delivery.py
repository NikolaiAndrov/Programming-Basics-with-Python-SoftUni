chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

chicken_price = 10.35
fish_price = 12.40
vegan_price = 8.15
delivery_price = 2.50

total_chicken_price = chicken_menu * chicken_price
total_fish_price = fish_menu * fish_price
total_vegan_price = vegan_menu * vegan_price
expenditures = total_chicken_price + total_fish_price + total_vegan_price
desert = expenditures * 0.20
total_expenditures = total_chicken_price + total_fish_price + total_vegan_price + desert + delivery_price
print(total_expenditures)
