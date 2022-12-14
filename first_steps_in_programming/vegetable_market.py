vegetable_price = float(input())
fruit_price = float(input())
vegetable_weight = int(input())
fruit_weight = int(input())
vegetable_sum = vegetable_price * vegetable_weight
fruit_sum = fruit_price * fruit_weight
total_sum_eur = (vegetable_sum + fruit_sum) / 1.94
print(format(total_sum_eur, '.2f'))