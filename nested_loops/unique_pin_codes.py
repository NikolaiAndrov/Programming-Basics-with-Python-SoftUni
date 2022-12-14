n1 = int(input())
n2 = int(input())
n3 = int(input())

even1 = 1
even2 = 1
prime = 1

for i in range(1, n1 + 1):
    if i % 2 == 0:
        even1 = i
    else:
        continue
    for j in range(1, n2 + 1):
        if j == 2 or j == 3 or j == 5 or j == 7:
            prime = j
        else:
            continue
        for k in range(1, n3 + 1):
            if k % 2 == 0:
                even2 = k
            else:
                continue
            print(f"{even1} {prime} {even2}")
