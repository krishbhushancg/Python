print('''1 → Wi-Fi
2 → Bluetooth
3 → Mobile Data
4 → Airplane Mode
5 → Exit''')

setting=int(input("enter setting number: "))
match setting:
    case 1:
        print("You selected Wi=Fi")
    case 2:
        print("You selected Bluetooth")
    case 3:
        print("You selected Mobile Data")
    case 4:
        print("You selected Airplane Mode")
    case 5:
        print("Exit")
    case _:
        print("Invalid Setting")
