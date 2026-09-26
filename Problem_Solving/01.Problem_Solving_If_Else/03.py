#Q3
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

if num1>num2:
    print(f"{num1} is greater")
elif num2>num1:
    print(f"{num2} is greater")
elif num1==num2:
    print("both are equal")
else:
    print("invalid data please try again")