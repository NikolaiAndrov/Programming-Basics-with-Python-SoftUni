annual_fee = int(input())

shoes = annual_fee * 0.6
clothes = shoes * 0.8
ball = clothes / 4
other_things = ball / 5

total = annual_fee + shoes + clothes + ball + other_things

print(f"{total:.2f}")
