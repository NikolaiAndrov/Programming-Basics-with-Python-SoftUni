joinery_count = int(input())
joinery_type = input()
receiving = input()

current_price = joinery_count
is_valid = True

if joinery_count < 10:
    is_valid = False

if joinery_type == "90X130":
    current_price *= 110
    if 30 < joinery_count <= 60:
        current_price *= 0.95
    elif joinery_count > 60:
        current_price *= 0.92
elif joinery_type == "100X150":
    current_price *= 140
    if 40 < joinery_count <= 80:
        current_price *= 0.94
    elif joinery_count > 80:
        current_price *= 0.9
elif joinery_type == "130X180":
    current_price *= 190
    if 20 < joinery_count <= 50:
        current_price *= 0.93
    elif joinery_count > 50:
        current_price *= 0.88
elif joinery_type == "200X300":
    current_price *= 250
    if 25 < joinery_count <= 50:
        current_price *= 0.91
    elif joinery_count > 50:
        current_price *= 0.86

if receiving == "With delivery":
    current_price += 60

if joinery_count > 99:
    current_price *= 0.96

if is_valid:
    print(f"{current_price:.2f} BGN")
else:
    print("Invalid order")