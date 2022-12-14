juniors = int(input())
seniors = int(input())
route = input()

all_participants = juniors + seniors
juniors_charity = 0
seniors_charity = 0

if route == "trail":
    juniors_charity = juniors * 5.50
    seniors_charity = seniors * 7
elif route == "cross-country":
    juniors_charity = juniors * 8
    seniors_charity = seniors * 9.50
elif route == "downhill":
    juniors_charity = juniors * 12.25
    seniors_charity = seniors * 13.75
elif route == "road":
    juniors_charity = juniors * 20
    seniors_charity = seniors * 21.50

total_charity = juniors_charity + seniors_charity
total_charity *= 0.95

if all_participants >= 50 and route == "cross-country":
    total_charity *= 0.75

print(f"{total_charity:.2f}")