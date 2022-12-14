minutes = int(input())
seconds = int(input())
distance = float(input())
seconds_per_100 = int(input())

all_seconds = minutes * 60 + seconds
late = distance / 120
late *= 2.5
the_time = (distance / 100) * seconds_per_100 - late

if the_time <= all_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {the_time:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(all_seconds - the_time):.3f} second slower.")
