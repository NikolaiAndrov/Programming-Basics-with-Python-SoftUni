first_player = int(input())
second_player = int(input())

input_line = input()
flag = True
while input_line != "End":

    if input_line == "one":
        second_player -= 1
    elif input_line == "two":
        first_player -= 1

    if first_player == 0:
        print(f"Player one is out of eggs. Player two has {second_player} eggs left.")
        flag = False
        break
    elif second_player == 0:
        print(f"Player two is out of eggs. Player one has {first_player} eggs left.")
        flag = False
        break

    input_line = input()

if flag:
    print(f"Player one has {first_player} eggs left.")
    print(f"Player two has {second_player} eggs left.")
