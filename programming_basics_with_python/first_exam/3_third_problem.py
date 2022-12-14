days_count = int(input())
room_type = input()
estimate = input()

price = days_count - 1

if room_type == "room for one person":
    price *= 18
elif room_type == "apartment":
    price *= 25
    if days_count < 10:
        price *= 0.7
    elif 10 <= days_count <= 15:
        price *= 0.65
    elif days_count > 15:
        price *= 0.5
elif room_type == "president apartment":
    price *= 35
    if days_count < 10:
       price *= 0.9
    elif 10 <= days_count <= 15:
        price *= 0.85
    elif days_count > 15:
        price *= 0.8

if estimate == "positive":
    price *= 1.25
elif estimate == "negative":
    price *= 0.9

print(f"{price:.2f}")