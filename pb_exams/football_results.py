first_result = input()
second_result = input()
third_result = input()
win = 0
lose = 0
drawn = 0

a = int(first_result[0])
b = int(second_result[0])
l = int(third_result[0])

e = int(first_result[2])
n = int(second_result[2])
i = int(third_result[2])

if a > e:
    win += 1
elif e > a:
    lose += 1
elif a == e:
    drawn += 1

if b > n:
    win += 1
elif n > b:
    lose += 1
elif b == n:
    drawn += 1

if l > i:
    win += 1
elif i > l:
    lose += 1
elif l == i:
    drawn += 1

print(f"Team won {win} games.")
print(f"Team lost {lose} games.")
print(f"Drawn games: {drawn}")
