print("1 → Regular  2 → Premium  3 → VIP")
type=int(input("enter account type: "))


match type:
    case 1:
        age=int(input("enter age: "))
        if age<5:
            print("Free Entry")
        else:
            print("regular")
    case 2:
        age=int(input("enter age: "))
        if age<5:
            print("Free Entry")
        else:
            print("premium")
    case 3:
        age=int(input("enter age: "))
        if age<5:
            print("Free Entry")
        else:
            print("VIP")
    case _:
        print("Invalid")