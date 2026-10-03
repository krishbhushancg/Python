print('''1 → Morning Show
2 → Afternoon Show
3 → Evening Show
4 → Night Show''')

movie=int(input("enter movie number: "))
match movie:
    case 1:
        print("Morning show selected")
    case 2:
        print("Afternoon show selected")
    case 3:
        print("Evening show selected")
    case 4:
       print("Night show selected")
    case _:
        print("Invalid")
