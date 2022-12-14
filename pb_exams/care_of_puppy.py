food_amount = int(input()) * 1000
eaten_food = 0

while True:
    line = input()
    if line == "Adopted":
        break
    line = int(line)
    eaten_food += line

if food_amount >= eaten_food:
    print(f"Food is enough! Leftovers: {food_amount - eaten_food} grams.")
else:
    print(f"Food is not enough. You need {eaten_food - food_amount} grams more.")
