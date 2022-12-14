import math

easter_bred = int(input())
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0


for i in range(easter_bred):
    sugar = int(input())
    flour = int(input())
    total_sugar += sugar
    total_flour += flour
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

sugar_pack = math.ceil(total_sugar / 950)
flour_pack = math.ceil(total_flour / 750)

print(f"Sugar: {sugar_pack}")
print(f"Flour: {flour_pack}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
