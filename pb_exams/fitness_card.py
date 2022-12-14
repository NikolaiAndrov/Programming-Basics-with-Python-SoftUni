budget = float(input())
gender = input()
age = int(input())
sport = input()
sport_price = 0

if sport == "Gym":
    if gender == "m":
        sport_price = 42
    elif gender == "f":
        sport_price = 35

elif sport == "Boxing":
    if gender == "m":
        sport_price = 41
    elif gender == "f":
        sport_price = 37

elif sport == "Yoga":
    if gender == "m":
        sport_price = 45
    elif gender == "f":
        sport_price = 42

elif sport == "Zumba":
    if gender == "m":
        sport_price = 34
    elif gender == "f":
        sport_price = 31

elif sport == "Dances":
    if gender == "m":
        sport_price = 51
    elif gender == "f":
        sport_price = 53

elif sport == "Pilates":
    if gender == "m":
        sport_price = 39
    elif gender == "f":
        sport_price = 37

if age <= 19:
    sport_price -= sport_price * 0.2

if budget >= sport_price:
    print(f"You purchased a 1 month pass for {sport}.")
elif sport_price > budget:
    print(f"You don't have enough money! You need ${sport_price - budget:.2f} more.")