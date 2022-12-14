length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height / 1000
capacity_occupied = percent / 100
liters_needed = volume * (1 - capacity_occupied)
print(liters_needed)