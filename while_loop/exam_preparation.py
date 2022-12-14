bad_grades = int(input())
problem = input()

bad_grades_count = 0
average = 0
all_problems = 0
last_problem = ""
many_bad_grades = False

while problem != "Enough":
    all_problems += 1
    last_problem = problem
    grade = int(input())
    average += grade
    if grade <= 4:
        bad_grades_count += 1
    if bad_grades_count == bad_grades:
        many_bad_grades = True
        break
    problem = input()

if many_bad_grades:
    print(f"You need a break, {bad_grades_count} poor grades.")
else:
    print(f"Average score: {average / all_problems:.2f}")
    print(f"Number of problems: {all_problems}")
    print(f"Last problem: {last_problem}")