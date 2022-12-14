input_line = input()
prime_numbers = 0
non_prime_numbers = 0

while input_line != "stop":
    input_line = int(input_line)
    count = 0

    if input_line < 0:
        print("Number is negative.")
        input_line = input()
        continue

    for i in range(1, input_line + 1):
        if input_line % i == 0:
            count += 1

    if count == 2:
        prime_numbers += input_line
    else:
        non_prime_numbers += input_line

    input_line = input()

print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {non_prime_numbers}")
