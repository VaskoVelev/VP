operations = ["+", "-", "*", "/"]

a = float(input("a = "))
b = float(input("b = "))

operation = ""
while operation not in operations:
    operation = input("operation: ")

    if operation == "/" and b == 0:
        while operation == "/":
            operation = input("operation: ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
else:
    result = a / b

print(f"{result:.3f}")