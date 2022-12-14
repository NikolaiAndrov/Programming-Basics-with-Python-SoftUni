bitcoin = int(input())
chinese_yuan = float(input())
commission = float(input())

bitcoin_leva = bitcoin * 1168
yuan_dollar = chinese_yuan * 0.15

sum_leva = bitcoin_leva + (yuan_dollar * 1.76)
sum_euro = sum_leva / 1.95
sum_euro -= sum_euro * (commission / 100)

print(f"{sum_euro:.2f}")
