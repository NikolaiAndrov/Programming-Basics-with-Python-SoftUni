steps = input()
all_steps = 0

while steps != "Going home":
    steps = int(steps)
    all_steps += steps

    if all_steps >= 10000:
        break
    steps = input()

if steps == "Going home":
    steps_to_home = int(input())
    all_steps += steps_to_home

diff = abs(10000 - all_steps)

if all_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
