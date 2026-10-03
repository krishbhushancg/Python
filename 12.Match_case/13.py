print('''1 → Monday
2 → Tuesday
3 → Wednesday
4 → Thursday
5 → Friday
6 → Saturday
7 → Sunday''')
day=int(input("enter day number: "))

match day:
    case 1:
        print("Weekday")
    case 2:
        print("Weekday")
    case 3:
        print("Weekday")
    case 4:
        print("Weekday")
    case 5:
        print("Weekday")
    case 6|7:
        print("Weekend")
    case _:
        print("Invalid")
