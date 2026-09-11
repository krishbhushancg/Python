#Q1
num1=int(input("enter first num: "))
num2=int(input("enter second number: "))

if num1>num2 :
    print(f"{num1} is greater")

elif num2>num1 :
    print(f"{num2} is greater")


#Q2
marks=int(input("enter your marks: "))
if 90 <= marks <= 100:
    print("Excellent")
elif 75 <= marks < 90:
    print("Good")
elif 50 <= marks < 75:
    print("Pass")
else:
    print("Fail")

#Q3
length=int(input("enter length: "))
width=int(input("enter width: "))
area=length*width
perimeter=2*(length+width)
print(f'''area of rectangle: {area}
perimeter of rectangle: {perimeter}''')

#Q4
a=int(input("enter number: "))
if a>0 :
    print("number is positive")
elif a<0:
    print("number is negative")
else:
    print("number is zero")

#Q5
price=int(input("enter the price: "))
dis_price=(price-(10/100*price))

if price>=1000:
    print("discount offered - 10%")
    print(f"final price offered {dis_price}")
else:
    print("no discount")

#Q6
python=int(input("enter your marks in python: "))
java=int(input("enter your marks in java: "))
css=int(input("enter your marks in css: "))

avg=((python+java+css)/3)
if avg>=40:
    print("Pass")
else:
    print("Fail")
