moves = int(input())

points = 0
zero_to_nine = 0
ten_to_nineteen = 0
twenty_to_twentynine = 0
thirty_to_thirtynine = 0
forty_to_fifty = 0
invalid_num = 0


for i in range(moves):
    number = int(input())
    if 0 <= number <= 9:
        points += number * 0.2
        zero_to_nine += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        ten_to_nineteen += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        twenty_to_twentynine += 1
    elif 30 <= number <= 39:
        points += 50
        thirty_to_thirtynine += 1
    elif 40 <= number <= 50:
        points += 100
        forty_to_fifty += 1
    else:
        points /= 2
        invalid_num += 1

print(f"{points:.2f}")
print(f"From 0 to 9: {(zero_to_nine / moves * 100):.2f}%")
print(f"From 10 to 19: {(ten_to_nineteen / moves * 100):.2f}%")
print(f"From 20 to 29: {(twenty_to_twentynine / moves * 100):.2f}%")
print(f"From 30 to 39: {(thirty_to_thirtynine / moves * 100):.2f}%")
print(f"From 40 to 50: {(forty_to_fifty / moves * 100):.2f}%")
print(f"Invalid numbers: {(invalid_num / moves * 100):.2f}%")
