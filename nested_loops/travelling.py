destination = input()
destination_to_go = ""
saved_sum = 0

while destination != "End":
    destination_to_go = destination
    sum_needed = float(input())

    while True:
        current_sum = float(input())
        saved_sum += current_sum
        if saved_sum >= sum_needed:
            print(f"Going to {destination_to_go}!")
            break
    saved_sum = 0
    destination = input()
