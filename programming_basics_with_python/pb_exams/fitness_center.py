people = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
work_out = 0
protein = 0

for i in range(people):
    input_line = input()
    if input_line == "Back":
        back += 1
        work_out += 1
    elif input_line == "Chest":
        chest += 1
        work_out += 1
    elif input_line == "Legs":
        legs += 1
        work_out += 1
    elif input_line == "Abs":
        abs += 1
        work_out += 1
    elif input_line == "Protein shake":
        protein_shake += 1
        protein += 1
    elif input_line == "Protein bar":
        protein_bar += 1
        protein += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_out / people * 100:.2f}% - work out")
print(f"{protein / people * 100:.2f}% - protein")
