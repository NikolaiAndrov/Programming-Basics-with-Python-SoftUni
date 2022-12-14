first_first = int(input())
first_second = int(input())
second_first = int(input())
second_second = int(input())

counter = 0
first_num = 0
second_num = 0


for i in range(first_first , 9):
    if counter == 6:
        break
    for j in range(9, first_second - 1, -1):
        if counter == 6:
            break
        for k in range(second_first, 9):
            if counter == 6:
                break
            for l in range(9, second_second - 1, -1):

                if i % 2 == 0 and j % 2 != 0 and k % 2 == 0 and l % 2 != 0:
                    first_num = (i * 10) + j
                    second_num = (k * 10) + l
                    if first_num == second_num:
                        print("Cannot change the same player.")
                    else:
                        counter += 1
                        print(f"{first_num} - {second_num}")
                        if counter == 6:
                            break
