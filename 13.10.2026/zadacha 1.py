n = 0
while n <= 0:
    n = int(input("n = "))

max = int(input("number1: "))
for i in range(n - 1):
    num = int(input(f"number{i + 2}: "))

    if num > max:
        max = num

print(max)