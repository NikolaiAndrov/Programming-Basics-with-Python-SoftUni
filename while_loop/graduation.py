name = input()

positive_grades = 0
negative_grades = 0
average_grade = 0

while True:
    grade = float(input())
    if grade >= 4:
        positive_grades += 1
        average_grade += grade
    else:
        negative_grades += 1

    if positive_grades >= 12:
        print(f"{name} graduated. Average grade: {average_grade / 12:.2f}")
        break
    if negative_grades >= 2:
        print(f"{name} has been excluded at {positive_grades + 1} grade")
        break