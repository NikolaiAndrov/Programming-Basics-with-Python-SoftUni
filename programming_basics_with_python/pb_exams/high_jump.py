desired_height = int(input())
starting_height = desired_height - 30
counter = 0
final_jump = 0
jumps = 0
success = True

while True:
    current_jump = int(input())
    jumps += 1
    if current_jump > starting_height:
        starting_height += 5
        counter = 0
    else:
        counter += 1

    final_jump = starting_height

    if counter == 3:
        success = False
        break

    if starting_height > desired_height:
        break

if success:
    print(f"Tihomir succeeded, he jumped over {desired_height}cm after {jumps} jumps.")
else:
    print(f"Tihomir failed at {final_jump}cm after {jumps} jumps.")
