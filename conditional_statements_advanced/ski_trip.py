stay_count = int(input())
place = input()
feedback = input()

stay_count -= 1
price = 0

if place == "room for one person":
    price = stay_count * 18
elif place == "apartment":
    price = stay_count * 25
    if stay_count < 10:
        price *= 0.7
    elif 10 <= stay_count <= 15:
        price *= 0.65
    elif stay_count > 15:
        price *= 0.5
elif place == "president apartment":
    price = stay_count * 35
    if stay_count < 10:
        price *= 0.9
    elif 10 <= stay_count <= 15:
        price *= 0.85
    elif stay_count > 15:
        price *= 0.8

if feedback == "positive":
    price *= 1.25
elif feedback == "negative":
    price *= 0.9

print(f"{price:.2f}")