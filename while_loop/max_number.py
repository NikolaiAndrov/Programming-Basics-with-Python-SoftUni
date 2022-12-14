import sys
max_num = -sys.maxsize

while True:
    n = input()
    if n == "Stop":
        break
    n = int(n)

    if n > max_num:
        max_num = n

print(max_num)