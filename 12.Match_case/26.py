print('''1 → Light
2 → Fan
3 → AC
4 → TV''')
type=int(input("enter device: "))


match type:
    case 1:
        print("light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid")