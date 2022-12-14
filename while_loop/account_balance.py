total_sum = 0

while True:
    n = input()
    if n == "NoMoreMoney":
        break
    n = float(n)

    if n >= 0:
        total_sum += n
        print(f"Increase: {n:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {total_sum:.2f}")