flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egs_count = int(input())
yeast = int(input())

sugar_price = flour_price * 0.75
total_flour = flour_price * flour_kg
total_sugar = (flour_price * 0.75) * sugar_kg
total_egs = (flour_price * 1.1) * egs_count
total_yest = (sugar_price * 0.2) * yeast

total_sum = total_flour + total_sugar + total_egs + total_yest
print(f"{total_sum:.2f}")
