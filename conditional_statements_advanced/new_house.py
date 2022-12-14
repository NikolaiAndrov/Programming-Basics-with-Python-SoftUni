flowers = input()
flowers_count = int(input())
budget = int(input())

price = 0

if flowers == "Roses":
    if flowers_count <= 80:
        price = flowers_count * 5
    else:
        price = (flowers_count * 5) * 0.9
elif flowers == "Dahlias":
    if flowers_count <= 90:
        price = flowers_count * 3.80
    else:
        price = (flowers_count * 3.80) * 0.85
elif flowers == "Tulips":
    if flowers_count <= 80:
        price = flowers_count * 2.80
    else:
        price = (flowers_count * 2.80) * 0.85
elif flowers == "Narcissus":
    if flowers_count < 120:
        price = (flowers_count * 3) * 1.15
    else:
        price = flowers_count * 3
elif flowers == "Gladiolus":
    if flowers_count < 80:
        price = (flowers_count * 2.50) * 1.2
    else:
        price = flowers_count * 2.50

diff = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")