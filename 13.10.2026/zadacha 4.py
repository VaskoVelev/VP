num = int(input("num = "))

is_prime = False

if num > 1:
    is_prime = True
    for i in range (2, num):
        if num % i == 0:
            is_prime = False

if is_prime:
    print("The number is prime")
else:
    print("The number is not prime")