n = int(input())
count = 0
flag = False

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if count == n:
            flag = True
            break
        count += 1
        print(count, end=" ")
    if flag:
        break
    print()
