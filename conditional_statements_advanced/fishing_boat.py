budget = int(input())
season = input()
fishermans = int(input())

expenditures = 0

if season == "Spring":
    if fishermans <= 6:
        expenditures = 3000 * 0.9
    elif 7 <= fishermans <= 11:
        expenditures = 3000 * 0.85
    elif fishermans >= 12:
        expenditures = 3000 * 0.75
elif season == "Summer" or season == "Autumn":
    if fishermans <= 6:
        expenditures = 4200 * 0.9
    elif 7 <= fishermans <= 11:
        expenditures = 4200 * 0.85
    elif fishermans >= 12:
        expenditures = 4200 * 0.75
elif season == "Winter":
    if fishermans <= 6:
        expenditures = 2600 * 0.9
    elif 7 <= fishermans <= 11:
        expenditures = 2600 * 0.85
    elif fishermans >= 12:
        expenditures = 2600 * 0.75

if fishermans % 2 == 0 and season != "Autumn":
    expenditures = expenditures * 0.95

diff = abs(budget - expenditures)

if budget >= expenditures:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
