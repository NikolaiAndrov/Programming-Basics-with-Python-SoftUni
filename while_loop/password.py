name = input()
password = input()

while True:
    line = input()
    if line == password:
        print(f"Welcome {name}!")
        break
