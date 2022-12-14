size = input()
color = input()
count = int(input())

current_price = count

if size == "Large":
    if color == "Red":
        current_price *= 16
    elif color == "Green":
        current_price *= 12
    elif color == "Yellow":
        current_price *= 9
elif size == "Medium":
    if color == "Red":
        current_price *= 13
    elif color == "Green":
        current_price *= 9
    elif color == "Yellow":
        current_price *= 7
elif size == "Small":
    if color == "Red":
        current_price *= 9
    elif color == "Green":
        current_price *= 8
    elif color == "Yellow":
        current_price *= 5

current_price *= 0.65

print(f"{current_price:.2f} leva.")
