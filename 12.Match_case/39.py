print('''1 → Employee
2 → Manager''')

category=int(input("enter identity: "))
match category:
    case 1:
        print('''1 → View Profile
2 → Apply Leave
3 → View Salary''')
        action=int(input("enter action: "))

        match action:
            case 1:
                print("View Profile selected")
            case 2:
                days=int(input("enter number of leave days: "))
                if days>0:
                    print("leave request submitted")
                else:
                    print("Invalid Leave Days")
            case _:
                print("View Salary")
            
    case 2:
            print('''1 → View Team
2 → Approve Leave
3 → View Reports''')
            action=int(input("enter lights name: "))

            match action:
                case 1:
                    print("View Team Selected")
                case 2:
                    print("Approve Leave Selected")
                case 3:
                    print("View Reports selected")
                case _:
                    print("Invalid")


    case _:
        print("Invalid")