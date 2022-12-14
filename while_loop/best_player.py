name = input()
winner = ""
max_goals = 0

while name != "END":
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        winner = name
    if goals >= 10:
        break

    name = input()

if max_goals >= 3:
    print(f"{winner} is the best player!")
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"{winner} is the best player!")
    print(f"He has scored {max_goals} goals.")
