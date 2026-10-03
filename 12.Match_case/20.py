a=int(input("enter number 1: "))
b=int(input("enter number 2: "))

print("1 → +  2 → - 3 → *  4 → /")

operation=int(input("enter operation number: "))
match operation:
    case 1:
        result=a+b
        print(f"result: {result}")
    case 2:
        result=a-b
        print(f"result: {result}")
    case 3:
        result=a*b
        print(f"result: {result}")
    case 4:
        if b==0:
            ("division by zero not possible")
        else:
            result=a/b    
        print(f"result: {result}")
    case _:
        print("Invalid")