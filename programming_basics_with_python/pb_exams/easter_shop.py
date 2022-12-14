egs = int(input())
input_line = input()

all_egs = egs
eggs_sold = 0
you_can_buy = 0
is_closed = True

while input_line != "Close":

    current_egs = int(input())
    you_can_buy = all_egs
    if input_line == "Buy":
        all_egs -= current_egs
        if all_egs < 0:
            is_closed = False
            break
        eggs_sold += current_egs
    elif input_line == "Fill":
        all_egs += current_egs

    input_line = input()

if is_closed:
    print(f"Store is closed!")
    print(f"{eggs_sold} eggs sold.")
else:
    print(f"Not enough eggs in store!")
    print(f"You can buy only {you_can_buy}.")
