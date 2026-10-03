print("1 → Student  2 → Teacher")
identity=int(input("enter identity: "))


match identity:
    case 1:
        print("1 → View Courses   2 → View Marks   3 → View Attendance")
        option=int(input("enter option number: "))
        match option:
            case 1:
                print("Opening Courses")
            case 2:
                print("Opening Marks")
            case 3:
                print("Opening Attendance")
            case _:
                    print("Invalid")

    case 2:
        print("1 → View Students   2 → View Marks   3 → View Attendance")
        options=int(input("enter option number: "))
        match options:
            case 1:
                print("Opening Courses")
            case 2:
                print("Opening Marks")
            case 3:
                print("Opening Attendance")
            case _:
                    print("Invalid")
        
    case _:
            print("Invalid")



