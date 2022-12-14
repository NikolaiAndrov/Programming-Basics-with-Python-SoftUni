walking_minutes = int(input())
walking_count = int(input())
calories_consumed = int(input())

all_walking_minutes = walking_minutes * walking_count
calories_burned = all_walking_minutes * 5
calories_left = calories_consumed / 2

if calories_burned >= calories_left:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")


