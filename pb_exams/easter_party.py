people = int(input())
price = float(input())
budget = float(input())

all_people_price = people * price

if 10 <= people <= 15:
    all_people_price *= 0.85
elif 15 < people <= 20:
    all_people_price *= 0.8
elif people > 20:
    all_people_price *= 0.75

cake = budget * 0.1

total_sum = all_people_price + cake
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")
