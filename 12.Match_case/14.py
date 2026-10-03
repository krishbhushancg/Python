print('''1 → Low
2 → Medium
3 → High
4 → Critical''')
day=int(input("enter priority number: "))

match day:
    case 1|2:
        print("Normal Priority")
    case 3|4:
        print("Urgent Priority")
    case _:
        print("Invalid")
