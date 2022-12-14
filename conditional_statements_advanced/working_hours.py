time = int(input())
day = input()

if 10 <= time <= 18:
    if day == "Monday":
        print("open")
    elif day == "Tuesday":
        print("open")
    elif day == "Wednesday":
        print("open")
    elif day == "Thursday":
        print("open")
    elif day == "Friday":
        print("open")
    elif day == "Saturday":
        print("open")
else:
    print("closed")

if day == "Sunday":
    print("closed")
