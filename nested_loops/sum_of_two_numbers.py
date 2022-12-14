start = int(input())
end = int(input())
magic_num = int(input())
counter = 0
flag = False

for i in range(start, end + 1):
    if flag:
        break
    for j in range(start, end + 1):
        counter += 1
        if i + j == magic_num:
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            flag = True
            break

if not flag:
    print(f"{counter} combinations - neither equals {magic_num}")



