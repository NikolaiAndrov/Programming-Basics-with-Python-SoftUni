company_name = input()
adult_tickets_count = int(input())
children_tickets_count = int(input())
adult_ticket_price = float(input())
tax_price = float(input())

one_children_ticket = (adult_ticket_price * 0.3) + tax_price
one_adult_ticket = adult_ticket_price + tax_price

total_children_tickets = one_children_ticket * children_tickets_count
total_adult_tickets = one_adult_ticket * adult_tickets_count
all_tickets_price = total_children_tickets + total_adult_tickets
profit = all_tickets_price * 0.2

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")
