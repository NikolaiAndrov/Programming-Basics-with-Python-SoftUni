balls = int(input())

points = 0
red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
black_count = 0
other_colors = 0

for i in range(balls):
    input_line = input()
    if input_line == "red":
        red_count += 1
        points += 5
    elif input_line == "orange":
        orange_count += 1
        points += 10
    elif input_line == "yellow":
        yellow_count += 1
        points += 15
    elif input_line == "white":
        white_count += 1
        points += 20
    elif input_line == "black":
        black_count += 1
        points /= 2
    else:
        other_colors += 1
        continue

print(f"Total points: {int(points)}")
print(f"Red balls: {red_count}")
print(f"Orange balls: {orange_count}")
print(f"Yellow balls: {yellow_count}")
print(f"White balls: {white_count}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {black_count}")
