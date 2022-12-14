tournament_name = input()

win = 0
lose = 0
all_tournaments = 0

while tournament_name != "End of tournaments":

    match_count = int(input())
    all_tournaments += match_count
    for i in range(1, match_count + 1):
        first_team_points = int(input())
        second_team_points = int(input())
        diff = abs(first_team_points - second_team_points)
        first_team_points -= second_team_points
        if first_team_points > 0:
            win += 1
            print(f"Game {i} of tournament {tournament_name}: win with {diff} points.")
        elif first_team_points < 0:
            lose += 1
            print(f"Game {i} of tournament {tournament_name}: lost with {diff} points.")

    tournament_name = input()

print(f"{win / all_tournaments * 100:.2f}% matches win")
print(f"{lose / all_tournaments * 100:.2f}% matches lost")