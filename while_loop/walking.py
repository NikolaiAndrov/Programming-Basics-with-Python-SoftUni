steps = input()
all_steps = 0
goal_reached = False

while steps != "Going home":
    steps = int(steps)
    all_steps += steps
    if all_steps >= 10000:
        goal_reached = True
        break
    steps = input()

if goal_reached:
    print("Goal reached! Good job!")
    print(f"{abs(10000 - all_steps)} steps over the goal!")
else:
    steps_to_go = int(input())
    all_steps += steps_to_go
    if all_steps >= 10000:
        print("Goal reached! Good job!")
        print(f"{abs(10000 - all_steps)} steps over the goal!")
    else:
        print(f"{abs(10000 - all_steps)} more steps to reach goal.")


