destination = input()
date = input()
nights = int(input())

current_price = nights

if destination == "France":
    if date == "21-23":
        current_price *= 30
    elif date == "24-27":
        current_price *= 35
    elif date == "28-31":
        current_price *= 40
elif destination == "Italy":
    if date == "21-23":
        current_price *= 28
    elif date == "24-27":
        current_price *= 32
    elif date == "28-31":
        current_price *= 39
elif destination == "Germany":
    if date == "21-23":
        current_price *= 32
    elif date == "24-27":
        current_price *= 37
    elif date == "28-31":
        current_price *= 43

print(f"Easter trip to {destination} : {current_price:.2f} leva.")