#Q29
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if (num1>num2 and num1<num3) or (num1>num3 and num1<num2):
    print(f"{num1} is the second largest")
elif (num2>num1 and num2<num3) or (num2>num3 and num2<num1):
    print(f"{num2} is the second largest")
elif (num3>num1 and num3<num2) or (num3<num1 and num3>num2):
    print(f"{num3} is the second largest")