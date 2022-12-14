days = int(input())
all_wins = 0
all_loses = 0
wins = 0
loses = 0
total_sum = 0
current_sum = 0
percent = 0

for i in range(days):
    game = input()
    while game != "Finish":
        if game == "win":
            all_wins += 1
            wins += 1
            total_sum += 20
            current_sum += 20
        elif game == "lose":
            all_loses += 1
            loses += 1

        game = input()

    if wins > loses:
        percent += current_sum * 0.1
    wins = 0
    loses = 0
    current_sum = 0

total_sum += percent

if all_wins > all_loses:
    total_sum *= 1.2
    print(f"You won the tournament! Total raised money: {total_sum:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_sum:.2f}")
