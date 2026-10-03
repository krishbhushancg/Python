print('''admin
teacher
student
guest''')
role=input("enter role: ").lower().strip()

match role:
    case "admin":
        print("Full Access")
    case "teacher":
        print("Teacher Dashboard")
    case "student":
        print("Student Dashboard")
    case "guest":
       print("Limited Access")
    case _:
        print("Invalid Role")

