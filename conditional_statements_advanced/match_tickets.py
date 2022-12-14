budget = float(input())
category = input()
people_count = int(input())

for_tickets = 0
for_transport = 0

if category == "VIP":
    for_tickets = people_count * 499.99
elif category == "Normal":
    for_tickets = people_count * 249.99

if 1 <= people_count <= 4:
    for_transport = budget * 0.75
elif 5 <= people_count <= 9:
    for_transport = budget * 0.6
elif 10 <= people_count <= 24:
    for_transport = budget * 0.5
elif 25 <= people_count <= 49:
    for_transport = budget * 0.4
elif people_count >= 50:
    for_transport = budget * 0.25

final_expenditures = (budget - for_tickets) - for_transport

if final_expenditures >= 0:
    print(f"Yes! You have {final_expenditures:.2f} leva left.")
else:
    final_expenditures = abs(final_expenditures)
    print(f"Not enough money! You need {final_expenditures:.2f} leva.")