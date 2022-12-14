chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0
tulips_price = 0
roses_price = 0
all_flowers = chrysanthemums + roses + tulips

# Spring, Summer, Аutumn, Winter

if season in ("Spring", "Summer"):
    chrysanthemums_price = chrysanthemums * 2
    roses_price = roses * 4.10
    tulips_price = tulips * 2.50
elif season in ("Autumn", "Winter"):
    chrysanthemums_price = chrysanthemums * 3.75
    roses_price = roses * 4.50
    tulips_price = tulips * 4.15

all_flowers_price = chrysanthemums_price + tulips_price + roses_price

if holiday == "Y":
    all_flowers_price *= 1.15

if tulips > 7 and season == "Spring":
    all_flowers_price *= 0.95
elif roses >= 10 and season == "Winter":
    all_flowers_price *= 0.9
if all_flowers > 20:
    all_flowers_price *= 0.8

all_flowers_price += 2

print(f"{all_flowers_price:.2f}")
