season = input()
kilometers = float(input())

price_for_km = 0

if kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        price_for_km = (kilometers * 0.75) * 4
    elif season == "Summer":
        price_for_km = (kilometers * 0.90) * 4
    elif season == "Winter":
        price_for_km = (kilometers * 1.05) * 4

elif 5000 < kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        price_for_km = (kilometers * 0.95) * 4
    elif season == "Summer":
        price_for_km = (kilometers * 1.10) * 4
    elif season == "Winter":
        price_for_km = (kilometers * 1.25) * 4

elif 10000 < kilometers <= 20000:
    price_for_km = (kilometers * 1.45) * 4

price_for_km *= 0.90

print(f"{price_for_km:.2f}")
