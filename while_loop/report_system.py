the_sum = int(input())
input_line = input()
iterations = 0
amount_saved = 0
cash_counter = 0
cash_sum = 0
cards_counter = 0
cards_sum = 0
sold = False

while input_line != "End":
    iterations += 1
    input_line = int(input_line)

    if iterations % 2 != 0:
        if input_line > 100:
            print("Error in transaction!")
        else:
            cash_counter += 1
            cash_sum += input_line
            amount_saved += input_line
            print("Product sold!")
    elif iterations % 2 == 0:
        if input_line < 10:
            print("Error in transaction!")
        else:
            cards_counter += 1
            cards_sum += input_line
            amount_saved += input_line
            print("Product sold!")

    if amount_saved >= the_sum:
        sold = True
        break

    input_line = input()

if sold:
    print(f"Average CS: {cash_sum / cash_counter:.2f}")
    print(f"Average CC: {cards_sum / cards_counter:.2f}")
else:
    print("Failed to collect required money for charity.")