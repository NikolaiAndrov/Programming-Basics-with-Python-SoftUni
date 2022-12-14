students = int(input())

all_grades = 0
fail = 0
between_three = 0
between_four = 0
top_students = 0

for i in range(students):
    grade = float(input())
    all_grades += grade
    if 2.00 <= grade <= 2.99:
        fail += 1
    elif 3.00 <= grade <= 3.99:
        between_three += 1
    elif 4.00 <= grade <= 4.99:
        between_four += 1
    elif 5.00 <= grade <= 6.00:
        top_students += 1


all_grades_percent = all_grades / students
fail_percent = (fail / students) * 100
between_three_percent = (between_three / students) * 100
between_four_percent = (between_four / students) * 100
top_students_percent = (top_students / students) * 100

print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_four_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_three_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {all_grades_percent:.2f}")
