town = input()
sales = float(input())
comission = 0

if 0 <= sales <= 500:
    if town == "Sofia":
        comission = sales * 0.05
    elif town == "Varna":
        comission = sales * 0.045
    elif town == "Plovdiv":
        comission = sales * 0.055
elif 500 < sales <= 1000:
    if town == "Sofia":
        comission = sales * 0.07
    elif town == "Varna":
        comission = sales * 0.075
    elif town == "Plovdiv":
        comission = sales * 0.08
elif 1000 < sales <= 10000:
    if town == "Sofia":
        comission = sales * 0.08
    elif town == "Varna":
        comission = sales * 0.1
    elif town == "Plovdiv":
        comission = sales * 0.12
elif sales > 10000:
    if town == "Sofia":
        comission = sales * 0.12
    elif town == "Varna":
        comission = sales * 0.13
    elif town == "Plovdiv":
        comission = sales * 0.145

if comission == 0:
    print("error")
else:
    print(f"{comission:.2f}")