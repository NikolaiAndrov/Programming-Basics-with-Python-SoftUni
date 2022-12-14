budget = float(input())
season = input()

place = ""
destination = ""
price = 0

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        destination = "Morocco"
        price = budget * 0.45

elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        destination = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    place = "Hotel"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        destination = "Morocco"
        price = budget * 0.90

print(f"{destination} - {place} - {price:.2f}")
