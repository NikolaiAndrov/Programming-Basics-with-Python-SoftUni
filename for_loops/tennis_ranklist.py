import math

tournir_count = int(input())
initial_points = int(input())

all_points = 0
win_count = 0

for i in range(tournir_count):
    stage = input()
    if stage == "W":
        win_count += 1
        all_points += 2000
    elif stage == "F":
        all_points += 1200
    elif stage == "SF":
        all_points += 720

total_points = initial_points + all_points
average_points = all_points / tournir_count
win_percent = (win_count / tournir_count) * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{win_percent:.2f}%")