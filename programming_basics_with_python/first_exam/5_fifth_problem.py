input_line = input()

all_meters = 5364
days = 1
success = False

while input_line != "END":
    current_meters = int(input())

    if input_line == "Yes":
        days += 1
        if days > 5:
            break
        all_meters += current_meters
    elif input_line == "No":
        all_meters += current_meters

    if all_meters >= 8848:
        success = True
        break

    input_line = input()

if success:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(all_meters)




