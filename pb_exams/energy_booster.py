fruit = input()
size = input()
set_count = int(input())
price = 0

if fruit == "Watermelon":
    if size == "big":
        price = (5 * 28.70) * set_count
    elif size == "small":
        price = (2 * 56) * set_count
elif fruit == "Mango":
    if size == "big":
        price = (5 * 19.60) * set_count
    elif size == "small":
        price = (2 * 36.66) * set_count
elif fruit == "Pineapple":
    if size == "big":
        price = (5 * 24.80) * set_count
    elif size == "small":
        price = (2 * 42.10) * set_count
elif fruit == "Raspberry":
    if size == "big":
        price = (5 * 15.20) * set_count
    elif size == "small":
        price = (2 * 20) * set_count

if 400 <= price <= 1000:
    price -= price * 0.15
elif price > 1000:
    price -= price * 0.5

print(f"{price:.2f} lv.")
