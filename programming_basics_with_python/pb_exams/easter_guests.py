import math
people = int(input())
budget = int(input())

buns_needed = math.ceil(people / 3)
egs_needed = people * 2
buns_price = buns_needed * 4
egs_price = egs_needed * 0.45
total_sum = buns_price + egs_price
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Lyubo bought {buns_needed} Easter bread and {egs_needed} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
