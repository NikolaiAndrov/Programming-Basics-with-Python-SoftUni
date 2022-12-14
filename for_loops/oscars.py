actor_name = input()
initial_points = float(input())
rate_persons_count = int(input())

evaluation = 0
evaluation += initial_points
for i in range(rate_persons_count):
    if evaluation >= 1250.5:
        break
    name = input()
    points = float(input())
    evaluation += (len(name) * points) / 2


if evaluation >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {evaluation:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - evaluation:.1f} more!")

