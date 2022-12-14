width = int(input())
height = int(input())
the_whole_cake = width * height
pieces = input()
cake_eaten = False

while pieces != "STOP":
    pieces = int(pieces)
    the_whole_cake -= pieces
    if the_whole_cake <= 0:
        cake_eaten = True
        break

    pieces = input()

if cake_eaten:
    print(f"No more cake left! You need {abs(the_whole_cake)} pieces more.")
else:
    print(f"{the_whole_cake} pieces are left.")
