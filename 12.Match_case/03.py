print('''1 → Check Balance
2 → Withdraw Money
3 → Deposit Money
4 → Change PIN
5 → Exit''')
atm=int(input("enter atm number: "))
match atm:
    case 1:
        print("Check Balance selected")
    case 2:
        print("Withdraw money selected")
    case 3:
        print("Deposit money selected")
    case 4:
        print("Change Pin selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid")
