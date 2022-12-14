pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())

pen_price = pens * 5.80
marker_price = markers * 7.20
detergent_price = detergent * 1.20
total_price = pen_price + marker_price + detergent_price
discounted_price = total_price - (total_price * discount / 100)
print(discounted_price)