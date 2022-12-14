days_count = int(input())

all_liters = 0
all_degrees = 0

for i in range(days_count):
    rakia_amount = float(input())
    degrees = float(input())

    all_liters += rakia_amount
    all_degrees += degrees * rakia_amount

avg_degree = all_degrees / all_liters

print(f"Liter: {all_liters:.2f}")
print(f"Degrees: {avg_degree:.2f}")

if avg_degree < 38:
    print(f"Not good, you should baking!")
elif 38 <= avg_degree <= 42:
    print("Super!")
elif avg_degree > 42:
    print("Dilution with distilled water!")