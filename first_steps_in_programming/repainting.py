nylon_sm = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())

additional_paint = paint * 0.1
nylon_bag = 0.40

nylon_price = (nylon_sm + 2) * 1.50
paint_price = (paint + additional_paint) * 14.50
diluent_price = diluent * 5.00

total_price = nylon_price + paint_price + diluent_price + nylon_bag
craftsman_price = (total_price * 0.3) * hours
total_expenditures = total_price + craftsman_price
print(total_expenditures)