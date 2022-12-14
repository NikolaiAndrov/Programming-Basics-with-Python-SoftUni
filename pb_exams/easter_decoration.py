clients = int(input())
items_count = 0
basket_count = 0
wreath_count = 0
chocolate_bunny_count = 0
bill = 0
avg_bill = 0

for i in range(clients):
    item = input()
    while item != "Finish":
        items_count += 1

        if item == "basket":
            basket_count += 1
        elif item == "wreath":
            wreath_count += 1
        elif item == "chocolate bunny":
            chocolate_bunny_count += 1

        item = input()

    bill = (basket_count * 1.50) + (wreath_count * 3.80) + (chocolate_bunny_count * 7)
    if items_count % 2 == 0:
        bill *= 0.8
    avg_bill += bill
    print(f"You purchased {items_count} items for {bill:.2f} leva.")

    items_count = 0
    basket_count = 0
    wreath_count = 0
    chocolate_bunny_count = 0
    bill = 0

print(f"Average bill per client is: {avg_bill / clients:.2f} leva.")