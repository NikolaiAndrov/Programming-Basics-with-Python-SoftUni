deposit = float(input())
term = int(input())
annual_interest_percent = float(input())

interest_sum = deposit * (annual_interest_percent / 100)
monthly_interest = interest_sum / 12
the_sum = deposit + term * monthly_interest
print(the_sum)
