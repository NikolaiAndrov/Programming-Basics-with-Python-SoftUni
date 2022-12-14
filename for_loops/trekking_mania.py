groups_count = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(groups_count):
    people = int(input())
    if people <= 5:
        musala += people
    elif 6 <= people <= 12:
        montblanc += people
    elif 13 <= people <= 25:
        kilimanjaro += people
    elif 26 <= people <= 40:
        k2 += people
    elif people >= 41:
        everest += people

all_people = musala + montblanc +kilimanjaro + k2 + everest

musala_percent = (musala / all_people) * 100
montblanc_percent = (montblanc / all_people) * 100
kilimanjaro_percent = (kilimanjaro / all_people) * 100
k2_percent = (k2 / all_people) * 100
everest_percent = (everest / all_people) * 100

print(f"{musala_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")