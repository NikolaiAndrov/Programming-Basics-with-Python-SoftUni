the_sum = float(input())
the_sum *= 100
coins = 0

while the_sum > 0:
    if the_sum >= 200:
        the_sum -= 200
    elif the_sum >= 100:
        the_sum -= 100
    elif the_sum >= 50:
        the_sum -= 50
    elif the_sum >= 20:
        the_sum -= 20
    elif the_sum >= 10:
        the_sum -= 10
    elif the_sum >= 5:
        the_sum -= 5
    elif the_sum >= 2:
        the_sum -= 2
    elif the_sum >= 1:
        the_sum -= 1
    else:
        break
    coins += 1

print(coins)
