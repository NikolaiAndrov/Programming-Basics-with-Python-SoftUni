eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0
max_eggs_color = ""

for i in range(1, eggs + 1):
    color = input()
    if color == "red":
        red += 1
    elif color == "orange":
        orange += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1

max_eggs = max(red, orange, blue, green)
if max_eggs is red:
    max_eggs_color = "red"
elif max_eggs is orange:
    max_eggs_color = "orange"
elif max_eggs is blue:
    max_eggs_color = "blue"
elif max_eggs is green:
    max_eggs_color = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_eggs_color}")
