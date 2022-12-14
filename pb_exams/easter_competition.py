easter_bred = int(input())
current_name = ""
current_points = 0
name = ""
max_points = 0

for i in range(1, easter_bred + 1):
    input_line = input()
    while input_line != "Stop":
        if input_line in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
            input_line = int(input_line)
            current_points += input_line
        else:
            current_name = input_line

        input_line = input()

    if current_points > max_points:
        max_points = current_points
        name = current_name
        print(f"{current_name} has {current_points} points.")
        print(f"{name} is the new number 1!")
    else:
        print(f"{current_name} has {current_points} points.")
    current_points = 0


print(f"{name} won competition with {max_points} points!")
