first_player = input()
second_player = input()
input_line = input()
first_player_points = 0
second_player_points = 0
war = False

while input_line != "End of game":
    first_card = int(input_line)
    second_card = int(input())

    if first_card > second_card:
        first_player_points += first_card - second_card
    elif second_card > first_card:
        second_player_points += second_card - first_card
    elif first_card == second_card:
        war = True
        first_card = int(input())
        second_card = int(input())
        if first_card > second_card:
            print("Number wars!")
            print(f"{first_player} is winner with {first_player_points} points")
            break
        elif second_card > first_card:
            print("Number wars!")
            print(f"{second_player} is winner with {second_player_points} points")
            break

    input_line = input()

if not war:
    print(f"{first_player} has {first_player_points} points")
    print(f"{second_player} has {second_player_points} points")