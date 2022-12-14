from math import ceil
movie_name = input()
movie_duration = int(input())
lunch_duration = int(input())

for_lunch = lunch_duration / 8
for_relax = lunch_duration / 4
busy_time = for_lunch + for_relax
time_left = lunch_duration - busy_time

if time_left >= movie_duration:
    print(f"You have enough time to watch {movie_name} and left with"
    f" {ceil(time_left - movie_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need "
    f"{ceil(movie_duration - time_left)} more minutes.")
