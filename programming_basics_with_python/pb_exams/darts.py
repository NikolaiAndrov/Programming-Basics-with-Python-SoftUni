name = input()
shot = input()
initial_points = 301
shots_count = 0
bad_shots_count = 0
win = False

while shot != "Retire":
    points = int(input())

    if shot == "Single":
        if initial_points >= points:
            initial_points -= points
            shots_count += 1
        else:
            bad_shots_count += 1
            shot = input()
            continue
    elif shot == "Double":
        points *= 2
        if initial_points >= points:
            initial_points -= points
            shots_count += 1
        else:
            bad_shots_count += 1
            shot = input()
            continue
    elif shot == "Triple":
        points *= 3
        if initial_points >= points:
            initial_points -= points
            shots_count += 1
        else:
            bad_shots_count += 1

    if initial_points == 0:
        win = True
        break

    shot = input()

if win:
    print(f"{name} won the leg with {shots_count} shots.")
else:
    print(f"{name} retired after {bad_shots_count} unsuccessful shots.")
