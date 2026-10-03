print("1 → Savings  2 → Current")
type=int(input("enter account type: "))

match type:
    case 1:
        print("savings account")
        print("1 → Check Balance   2 → Deposit   3 → Withdraw")
        operation=int(input("enter operation number: "))
        match operation:
            case 1:
                print("Check balance selected")
            case 2:
                print("deposit selected")
            case 3:
                print("Withdraw selected")
            case _:
                    print("Invalid")

    case 2:
        print("savings account")
        print("1 → Check Balance   2 → Deposit   3 → Withdraw")
        operation=int(input("enter operation number: "))
        match operation:
            case 1:
                print("Check balance selected")
            case 2:
                print("deposit selected")
            case 3:
                print("Withdraw selected")
            case _:
                print("Invalid")
                
    case _:
            print("Invalid")