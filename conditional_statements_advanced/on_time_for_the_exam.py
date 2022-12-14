exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

all_exam_min = (exam_hour * 60) + exam_min
all_arrival_min = (arrival_hour * 60) + arrival_min
diff = abs(all_arrival_min - all_exam_min)
# exam 9:30 = 570 < on time;   |   arrival 9:50 = 590 > late;

if all_arrival_min > all_exam_min:
    if diff >= 60:
        diff_in_hours = diff // 60
        diff_in_min = diff % 60
        print("late")
        print(f"{diff_in_hours}:{diff_in_min:02d} hours after the start")
    else:
        print("late")
        print(f"{diff} minutes after the start")
elif all_exam_min >= all_arrival_min and diff <= 30:
    if diff == 0:
        print("on time")
    else:
        print("on time")
        print(f"{diff} minutes before the start")
elif all_exam_min >= all_arrival_min and diff > 30:
    if diff >= 60:
        diff_in_hours = diff // 60
        diff_in_min = diff % 60
        print("Early")
        print(f"{diff_in_hours}:{diff_in_min:02d} hours before the start")
    else:
        print("Early")
        print(f"{diff} minutes before the start")


