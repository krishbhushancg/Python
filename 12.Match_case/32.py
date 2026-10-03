print('''1 → Student
2 → Teacher
3 → Parent''')

category=int(input("enter identity: "))
match category:
    case 1:
        print('''1 → Marks
2 → Attendance
3 → Homework''')
        action=int(input("enter action: "))

        match action:
            case 1:
                print("Marks Selected")
            case 2:
                print("Attendance Selected")
            case 3:
                print("Homework Selected")
            case _:
                print("Invalid")
            
    case 2:
            print('''1 → Enter Marks
2 → Attendance
3 → Assign Homework''')
            action=int(input("enter action: "))
    
            match action:
                case 1:
                    print("Enter Marks Selected")
                case 2:
                    print("Attendance Selected")
                case 3:
                    print("Assign Homework Selected")
                case _:
                    print("Invalid")

    case 3:
                print('''1 → Child Marks
2 → Child Attendance
3 → Contact Teacher''')
                action=int(input("enter action: "))
        
                match action:
                    case 1:
                        print("Child Marks Selected")
                    case 2:
                        print("Child Attendance Selected")
                    case 3:
                        print("Contact Teacher Selected")
                    case _:
                        print("Invalid")
    case _:
        print("Invalid")