tabs = int(input())
salary = int(input())

for i in range(tabs):
    web_site = input()
    if web_site == "Facebook":
        salary -= 150
    elif web_site == "Instagram":
        salary -= 100
    elif web_site == "Reddit":
        salary -= 50

    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
