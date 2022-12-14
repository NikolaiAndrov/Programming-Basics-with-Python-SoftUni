n = int(input())

is_valid = 100 <= n <= 200 or n == 0

if not is_valid:
    print("invalid")
