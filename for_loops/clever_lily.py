age = int(input())
laundry_price = float(input())
toys_price = int(input())

toys_count = 0
saved_money = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toys_count += 1
    else:
        saved_money += (i * 5) - 1

total_money = (toys_price * toys_count) + saved_money

diff = abs(laundry_price - total_money)

if total_money >= laundry_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
