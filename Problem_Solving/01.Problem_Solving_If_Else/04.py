#Q4
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))

if (num1<num2) and (num1<num3):
    print(f"{num1} is smallest")
elif (num2<num1) and (num2<num3):
    print(f"{num2} is smallest")
elif (num3<num2) and (num3<num1):
    print(f"{num3} is smallest")
else:
    print("invalid data")
