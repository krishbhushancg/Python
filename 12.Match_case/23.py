print("1 → Savings  2 → Current")
type=int(input("enter account type: "))


match type:
    case 1:
        print("savings account")
        amount=int(input("enter withdrawl amount: "))
        if amount>=0:
            print("withdrawl request accepted")
        else:
            print("invalid amount")

    case 2:
        print("current account")
        amount=int(input("enter withdrawl amount: "))
        if amount>=0:
            print("withdrawl request accepted")
        else:
            print("invalid amount")
           
    case _:
            print("Invalid")