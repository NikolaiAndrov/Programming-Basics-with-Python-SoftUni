import sys
n = int(input())
max_num = -sys.maxsize
sum_nums = 0

for i in range(n):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num

    sum_nums += current_num

if max_num == sum_nums - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    sum_nums -= max_num
    diff = abs(max_num - sum_nums)
    print("No")
    print(f"Diff = {diff}")