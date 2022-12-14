paper = int(input())
cloth = int(input())
glow = float(input())
discount = int(input())

paper_price = paper * 5.80
cloth_price = cloth * 7.20
glow_price = glow * 1.20

all_materials = paper_price + cloth_price + glow_price
discount_2 = discount / 100
after_discount = all_materials - (all_materials * discount_2)

print(f"{after_discount:.3f}")