jury = int(input())
presentation = input()
final_assessment = 0
grades_count = 0

while presentation != "Finish":
    current_grade = 0
    for i in range(jury):
        grade =  float(input())
        grades_count += 1
        current_grade += grade
        final_assessment += grade

    avg_grade = current_grade / jury
    print(f"{presentation} - {avg_grade:.2f}.")

    presentation = input()

print(f"Student's final assessment is {final_assessment / grades_count:.2f}.")