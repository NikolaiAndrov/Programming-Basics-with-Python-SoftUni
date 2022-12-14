vacation_cost = float(input())
available_money = float(input())

total_money = available_money
spend_count = 0
all_days = 0
spending_too_much = False

while total_money < vacation_cost:
    action = input()
    the_sum = float(input())
    all_days += 1

    if action == "spend":
        spend_count += 1
        if spend_count == 5:
            spending_too_much = True
            break
        total_money -= the_sum
        if total_money < 0:
            total_money = 0
    elif action == "save":
        total_money += the_sum
        spend_count = 0

if spending_too_much:
    print("You can't save the money.")
    print(all_days)
else:
    print(f"You saved the money for {all_days} days.")