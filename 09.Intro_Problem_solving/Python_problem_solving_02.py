# #Q1
# num1=int(input("enter first num: "))
# num2=int(input("enter second num: "))

# sum=(num1+num2)
# print(f"sum:{sum}")

# #Q2
# num=int(input("enter num: "))
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")

#Q3
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

if (a>b) and (a>c):
    print(f"{a} is the greatest")
elif (b>a) and (b>c):
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")

#Q4
age=int(input("enter age: "))
if age>=18:
    print("eligible to vote")

#Q5
price=int(input("enter the price: "))
dis_price=(price-(20/100*price))

if price>=2000:
    print("discount offered - 20%")
    print(f"final price offered {dis_price}")
else:
    print("no discount")

#Q6
