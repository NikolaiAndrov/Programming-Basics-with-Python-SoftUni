line = input()

sum_letters = 0

for i in line:
    if i == "a":
        sum_letters += 1
    if i == "e":
        sum_letters += 2
    if i == "i":
        sum_letters += 3
    if i == "o":
        sum_letters += 4
    if i == "u":
        sum_letters += 5

print(sum_letters)