projection = input()
rows = int(input())
cols = int(input())

all_seats = rows * cols
income = 0

if projection == "Premiere":
    income = all_seats * 12
elif projection == "Normal":
    income = all_seats * 7.5
elif projection == "Discount":
    income = all_seats * 5

print(f"{income:.2f}")
print("leva")

