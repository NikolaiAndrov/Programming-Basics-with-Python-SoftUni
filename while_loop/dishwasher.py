bottles = int(input())
dishes = input()
detergent = bottles * 750
detergent_dishes = 0
action_detergent = 0
iterations = 0
all_dishes = 0
all_pots = 0
flag = False


while dishes != "End":
    iterations += 1
    dishes = int(dishes)

    if iterations % 3 == 0:
        detergent_dishes += dishes * 15
        all_pots += dishes
    else:
        detergent_dishes += dishes * 5
        all_dishes += dishes

    action_detergent = detergent - detergent_dishes
    if action_detergent < 0:
        flag = True
        break

    dishes = input()

diff = abs(detergent - detergent_dishes)

if flag:
    print(f"Not enough detergent, {abs(action_detergent)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{all_dishes} dishes and {all_pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")