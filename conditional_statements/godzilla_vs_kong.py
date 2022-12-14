movie_budget = float(input())
actors_count = int(input())
clothes_price = float(input())

decor = movie_budget * 0.1
clothes_expenditures = actors_count * clothes_price
if actors_count > 150:
    clothes_expenditures -= clothes_expenditures * 0.1
total_sum = decor + clothes_expenditures

if movie_budget >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - total_sum:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_sum - movie_budget:.2f} leva more.")
