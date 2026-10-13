n = 0
while n <= 0:
    n = int(input("n = "))

sum = 0
for i in range(n):
    num = int(input(f"number{i + 1}: "))
    sum += num

print(sum)