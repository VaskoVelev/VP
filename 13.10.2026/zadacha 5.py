days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

num = 0
while num < 1 or num > 7:
    num = int(input("num = "))

print(f"{num}: {days[num]}")