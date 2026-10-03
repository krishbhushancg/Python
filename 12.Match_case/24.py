print("1 → Start Exam  2 → View Result  3 → Exit")
type=int(input("enter account type: "))


match type:
    case 1:
        age=int(input("enter age: "))
        if age>=18:
            print("You can start the exam")
        else:
            print("You cant start the exam")

    case 2:
        print("opening result")
    case 3:
        print("exiting...")
    case _:
        print("Invalid")