groups_count = int(input())

musala_climbers = 0
montblanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

for i in range(groups_count):
    person_count = int(input())
    if person_count <= 5:
        musala_climbers += person_count
    elif 6 <= person_count <= 12:
        montblanc_climbers += person_count
    elif 13 <= person_count <= 25:
        kilimanjaro_climbers += person_count
    elif 26 <= person_count <= 40:
        k2_climbers += person_count
    elif person_count >= 41:
        everest_climbers += person_count

all_climbers = musala_climbers + montblanc_climbers + kilimanjaro_climbers + k2_climbers + everest_climbers

musala_climbers_percent = (musala_climbers / all_climbers) * 100
montblanc_climbers_percent = (montblanc_climbers / all_climbers) * 100
kilimanjaro_climbers_percent = (kilimanjaro_climbers / all_climbers) * 100
k2_climbers_percent = (k2_climbers / all_climbers) * 100
everest_climbers_percent = (everest_climbers / all_climbers) * 100

print(f"{musala_climbers_percent:.2f}%")
print(f"{montblanc_climbers_percent:.2f}%")
print(f"{kilimanjaro_climbers_percent:.2f}%")
print(f"{k2_climbers_percent:.2f}%")
print(f"{everest_climbers_percent:.2f}%")
