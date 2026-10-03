print('''1 → UPI
2 → Card
3 → Wallet''')

category=int(input("enter category: "))
match category:
    case 1:
        print('''1 → Scan QR
2 → Enter UPI ID''')
        action=int(input("enter payment method: "))

        match action:
            case 1:
                print("Scanning QR..")
            case 2:
                print("UPI ID Selected")
            case _:
                print("Invalid")
            
    case 2:
            print('''1 → Credit Card
2 → Debit Card''')
            action=int(input("enter payment method: "))
    
            match action:
                case 1:
                    print("Credit Card Selected")
                case 2:
                    print("Debit Card Selected")
                case _:
                    print("Invalid")

    case 3:
                print('''1 → Add Money
2 → Pay Using Wallet''')
                action=int(input("enter payment method: "))
        
                match action:
                    case 1:
                        print("Adding money...")
                    case 2:
                        print("Paying Using Wallet")
                    case _:
                        print("Invalid")
    case _:
        print("Invalid")