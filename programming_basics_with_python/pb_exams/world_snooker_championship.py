championship = input()
ticket_type = input()
ticket_count = int(input())
photo = input()
price = ticket_count
photo_price = ticket_count * 40

if championship == "Quarter final":
    if ticket_type == "Standard":
        price *= 55.50
    elif ticket_type == "Premium":
        price *= 105.20
    elif ticket_type == "VIP":
        price *= 118.90
elif championship == "Semi final":
    if ticket_type == "Standard":
        price *= 75.88
    elif ticket_type == "Premium":
        price *= 125.22
    elif ticket_type == "VIP":
        price *= 300.40
elif championship == "Final":
    if ticket_type == "Standard":
        price *= 110.10
    elif ticket_type == "Premium":
        price *= 160.66
    elif ticket_type == "VIP":
        price *= 400

if 2500 < price <= 4000:
    price *= 0.9
if photo == "Y" and price <= 4000:
    price += photo_price
elif price > 4000:
    price *= 0.75

print(f"{price:.2f}")