print('''1 → Student
2 → Teacher
3 → Administration''')

role=int(input("enter identity: "))
match role:
    case 1:
        print('''1 → Profile
2 → Marks
3 → Attendance
4 → Courses''')
        action=int(input("enter action: "))

        match action:
            case 1:
                print("Profile selected")
            case 2:
                print("Marks Selected")
            case 3:
                print("Attendance Selected")
            case 4:
                print("Courses Selected")
            case _:
                print("Invalid")
            
    case 2:
            print('''1 → Students
2 → Enter Marks
3 → Attendance
4 → Courses''')
            action=int(input("enter action: "))

            match action:
                case 1:
                    print("Students Selected")
                case 2:
                    print("Enter Marks Selected")
                case 3:
                    print("Attendance selected")
                case 4:
                    print("Courses selected")
                case _:
                    print("Invalid")

    case 3:
                print('''1 → Fees
2 → Admissions
3 → Notices
4 → Departments''')
                action=int(input("enter action: "))
        
                match action:
                    case 1:
                        print("Fees selcted: ")
                    case 2:
                        print("Admissions selcted")
                    case 3:
                        print("Notices selected")
                    case 4:
                        print("Departments selected")
                    case _:
                        print("Invalid")
    case _:
        print("Invalid")