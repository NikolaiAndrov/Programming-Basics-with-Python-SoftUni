money = float(input())
years = int(input())

remaining_money = money
age = 17

for i in range(1800, years + 1):
    if i % 2 == 0:
        age += 1
        remaining_money -= 12000
    else:
        age += 1
        remaining_money = remaining_money - (12000 + 50 * age)

if remaining_money >= 0:
    print(f"Yes! He will live a carefree life and will have {remaining_money:.2f} dollars left.")
else:
    remaining_money = abs(remaining_money)
    print(f"He will need {remaining_money:.2f} dollars to survive.")
