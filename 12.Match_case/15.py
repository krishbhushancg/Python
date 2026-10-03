print('''1 → Bronze
2 → Silver
3 → Gold
4 → Platinum''')
membership=int(input("enter membership: "))

match membership:
    case 1|2:
        print("Basic Membership")
    case 3|4:
        print("Premium Membership")
    case _:
        print("Invalid")
