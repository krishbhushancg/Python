print('''1 → View Profile
2 → View Courses
3 → View Marks
4 → View Attendance
5 → Logout''')
student_portal=int(input("enter atm number: "))
match student_portal:
    case 1:
        print("Opening Profile")
    case 2:
        print("Opening Courses")
    case 3:
        print("Opening Marks")
    case 4:
        print("Opening Attendance")
    case 5:
        print("Logout")
    case _:
        print("Invalid")
