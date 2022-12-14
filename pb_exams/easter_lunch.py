easter_bred = int(input())
egs = int(input())
sweets = int(input())

easter_bred_price = easter_bred * 3.20
egs_price = egs * 4.35
sweets_price = sweets * 5.40
egs_paint = (egs * 12) * 0.15

total_sum = easter_bred_price + egs_price + sweets_price + egs_paint

print(f"{total_sum:.2f}")
