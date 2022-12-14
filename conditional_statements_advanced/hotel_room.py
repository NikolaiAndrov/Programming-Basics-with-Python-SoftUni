month = input()
stay_count = int(input())

studio_price = 0
apartment_price = 0

if month in("May", "October"):
    studio_price = stay_count * 50
    apartment_price = stay_count * 65
    if 7 < stay_count <= 14:
        studio_price *= 0.95
    elif stay_count > 14:
        studio_price *= 0.7
        apartment_price *= 0.9

elif month in("June", "September"):
    studio_price = stay_count * 75.20
    apartment_price = stay_count * 68.70
    if stay_count > 14:
        studio_price *= 0.8
        apartment_price *= 0.9

elif month in("July", "August"):
    studio_price = stay_count * 76
    apartment_price = stay_count * 77
    if stay_count > 14:
        apartment_price *= 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
