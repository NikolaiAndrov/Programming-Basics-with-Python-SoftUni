from math import floor
record_in_seconds = float(input())
distance_meters = float(input())
seconds_for_meter = float(input())

delay = (distance_meters // 50) * 30
sum_seconds = distance_meters * seconds_for_meter + delay

if sum_seconds >= record_in_seconds:
    print(f"No! He was {sum_seconds - record_in_seconds:.2f} seconds slower.")
else:
    print(f" Yes! The new record is {sum_seconds:.2f} seconds.")