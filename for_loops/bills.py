months = int(input())

electricity = 0
water = 0
internet = 0
other = 0
average = 0

for i in range(1, months + 1):
    el_bill = float(input())
    electricity += el_bill
    water += 20
    internet += 15

other = (electricity + water + internet) * 1.20
average = (electricity + water + internet + other) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")
