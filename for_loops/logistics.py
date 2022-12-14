loads = int(input())

all_tons = 0
bus = 0
truck = 0
train = 0

for i in range(loads):
    tons = int(input())
    all_tons += tons

    if tons <= 3:
        bus += tons
    elif 4 <= tons <= 11:
        truck += tons
    else:
        train += tons

average = (bus * 200 + truck * 175 + train * 120) / all_tons

bus_percent = (bus / all_tons) * 100
truck_percent = (truck / all_tons) * 100
train_percent = (train / all_tons) * 100

print(f"{average:.2f}")
print(f"{bus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")
