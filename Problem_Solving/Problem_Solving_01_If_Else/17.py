#Q17
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
print("5 for floor division")

operation_number=int(input("enter your operation: "))

a=int(input("enter first number: "))
b=int(input("enter second number: "))

if operation_number==1 or operation_number==2 or operation_number==3 or operation_number==4 or operation_number==5:

    if operation_number==1:
        print(a+b)

    elif operation_number==2:
        print(a-b)

    elif operation_number==3:
        print(a*b)

    elif operation_number==4:
        if b==0:
            print("division by zero is not possible")
        else:
            print(a/b)

    elif operation_number==5:
        print(a//b)

else:
    print("not a valid operation try again")