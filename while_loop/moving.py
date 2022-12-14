width = int(input())
length = int(input())
height = int(input())
the_whole_room = width * length * height

boxes = input()
is_fool = False

while boxes != "Done":
    boxes = int(boxes)
    the_whole_room -= boxes
    if the_whole_room <= 0:
        is_fool = True
        break
    boxes = input()

if is_fool:
    print(f"No more free space! You need {abs(the_whole_room)} Cubic meters more.")
else:
    print(f"{the_whole_room} Cubic meters left.")