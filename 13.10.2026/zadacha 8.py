min = float(input("min = "))

max = min
while max <= min:
    max = float(input("max = "))

count = 0
for i in range(10):
    num = float(input(f"number{i + 1} = "))
    if num >= min and num <= max:
        count += 1

print(count)