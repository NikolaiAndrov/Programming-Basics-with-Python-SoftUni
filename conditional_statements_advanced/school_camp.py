season = input()
group_type = input()
students_count = int(input())
stay_count = int(input())

price = 0
sport_type = ""

# Сезонът – текст - “Winter”, “Spring” или “Summer”;
# Видът на групата – текст - “boys”, “girls” или “mixed”;

if season == "Winter":
    if group_type == "boys":
        sport_type = "Judo"
        price = students_count * 9.60 * stay_count
    elif group_type == "girls":
        sport_type = "Gymnastics"
        price = students_count * 9.60 * stay_count
    elif group_type == "mixed":
        sport_type = "Ski"
        price = students_count * 10 * stay_count

elif season == "Spring":
    if group_type == "boys":
        sport_type = "Tennis"
        price = students_count * 7.20 * stay_count
    elif group_type == "girls":
        sport_type = "Athletics"
        price = students_count * 7.20 * stay_count
    elif group_type == "mixed":
        sport_type = "Cycling"
        price = students_count * 9.50 * stay_count

elif season == "Summer":
    if group_type == "boys":
        sport_type = "Football"
        price = students_count * 15 * stay_count
    elif group_type == "girls":
        sport_type = "Volleyball"
        price = students_count * 15 * stay_count
    elif group_type == "mixed":
        sport_type = "Swimming"
        price = students_count * 20 * stay_count

if 10 <= students_count < 20:
    price *= 0.95
elif 20 <= students_count < 50:
    price *= 0.85
elif students_count >= 50:
    price *= 0.50

print(f"{sport_type} {price:.2f} lv.")