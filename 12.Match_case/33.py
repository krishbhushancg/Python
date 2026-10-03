print('''1 → Flight
2 → Train
3 → Bus''')

transport=int(input("enter identity: "))
match transport:
    case 1:
        print('''1 → Economy
2 → Business''')
        seat=int(input("enter seat type: "))

        match seat:
            case 1:
                print("Economy Selected")
            case 2:
                print("Business Selected")
            case _:
                print("Invalid")
            
    case 2:
            print('''1 → Sleeper
2 → AC''')
            seat=int(input("enter seat type: "))
    
            match seat:
                case 1:
                    print("Sleeper Selected")
                case 2:
                    print("AC Selected")
                case _:
                    print("Invalid")

    case 3:
                print('''1 → Ordinary
2 → Volvo''')
                seat=int(input("enter seat type: "))
        
                match seat:
                    case 1:
                        print("Ordinary Selected")
                    case 2:
                        print("Volvo Selected")
                    case _:
                        print("Invalid")
    case _:
        print("Invalid")