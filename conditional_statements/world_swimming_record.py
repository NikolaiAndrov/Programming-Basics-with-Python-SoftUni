current_record = float(input())
distance_in_meter = float(input())
seconds_for_meter = float(input())

total_seconds = distance_in_meter * seconds_for_meter
delay = (distance_in_meter // 15) * 12.5
total_time = total_seconds + delay

if total_time >= current_record:
    print(f"No, he failed! He was {total_time - current_record:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")