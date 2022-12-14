n = int(input())
food_amount = float(input())

dog_sum_eaten_food = 0
cat_sum_eaten_food = 0
bonus = 0

for i in range(n):
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())
    dog_sum_eaten_food += dog_eaten_food
    cat_sum_eaten_food += cat_eaten_food
    if (i + 1) % 3 == 0:
        current_bonus = (dog_eaten_food + cat_eaten_food) * 0.1
        bonus += current_bonus

total_eaten_food = dog_sum_eaten_food + cat_sum_eaten_food
total_eaten_food_percent = (total_eaten_food / food_amount) * 100
dog_eaten_food_percent = (dog_sum_eaten_food / total_eaten_food) * 100
cat_eaten_food_percent = (cat_sum_eaten_food / total_eaten_food) * 100

print(f"Total eaten biscuits: {round(bonus)}gr.")
print(f"{total_eaten_food_percent:.2f}% of the food has been eaten.")
print(f"{dog_eaten_food_percent:.2f}% eaten from the dog.")
print(f"{cat_eaten_food_percent:.2f}% eaten from the cat.")
