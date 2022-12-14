capacity = float(input())
suitcase = input()
action_capacity = capacity
counter = 0
is_full = False

while suitcase != "End":
    counter += 1
    suitcase = float(suitcase)
    if counter % 3 == 0:
        suitcase = suitcase * 1.1

    action_capacity -= suitcase
    if action_capacity <= 0:
        is_full = True
        break

    suitcase = input()

if is_full:
    print("No more space!")
    print(f"Statistic: {counter - 1} suitcases loaded.")
else:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {counter} suitcases loaded.")
