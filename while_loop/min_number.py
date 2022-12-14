import sys
min_num = sys.maxsize

while True:
    n = input()
    if n == "Stop":
        break

    n = int(n)
    if n < min_num:
        min_num = n

print(min_num)