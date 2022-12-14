num1 = int(input())
num2 = int(input())
input_operator = input()

result = 0
flag = False

if input_operator == "+":
    result = num1 + num2
elif input_operator == "-":
    result = num1 - num2
elif input_operator == "*":
    result = num1 * num2
elif input_operator == "/":
    if num2 == 0:
        flag = True
    else:
        result = num1 / num2
elif input_operator == "%":
    if num2 == 0:
        flag = True
    else:
        result = num1 % num2

if input_operator in ("+", "-", "*") and result % 2 == 0:
    print(f"{num1} {input_operator} {num2} = {result} - even")
elif input_operator in ("+", "-", "*") and result % 2 == 1:
    print(f"{num1} {input_operator} {num2} = {result} - odd")

if input_operator in ("/", "%") and flag:
    print(f"Cannot divide {num1} by zero")
elif input_operator == "/":
    print(f"{num1} {input_operator} {num2} = {result:.2f}")
elif input_operator == "%":
    print(f"{num1} {input_operator} {num2} = {result}")
