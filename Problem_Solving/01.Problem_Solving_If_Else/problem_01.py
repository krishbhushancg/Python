#Q1
num=int(input("enter number: "))
if num>0:
    print("positive")
if num<0:
    print("negative")
if num==0:
    print("zero")

#Q2
num=int(input("enter number: "))
if num>0 and num%2==0:
    print("Positive and even")
if num>0 and num%2==1:
    print("Positive and odd")
if num<0 and num%2==0:
    print("Negative and even")
if num<0 and num%2==0:
    print("Negative and odd")
if num<0 and num%2==1:
    print("number is zero")

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

#Q4
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))

if (num1<num2) and (num1<num3):
    print(f"{num1} is smallest")
if (num2<num1) and (num2<num3):
    print(f"{num2} is smallest")
if (num3<num2) and (num3<num1):
    print(f"{num3} is smallest")
else:
    print("invalid data")

#Q5
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))

if (num1>num2) and (num1>num3):
    print(f"{num1} is greater")
if (num2>num1) and (num2>num3):
    print(f"{num2} is greater")
if (num3>num2) and (num3>num1):
    print(f"{num1} is greater")
else:
    print("invalid data")

#Q6
num=int(input("Enter number: "))
if (num%5==0) and (num%11==0):
    print(f"{num} is divisible by 5 and 11")
if (num%5!=0) and (num%11==0):
    print(f"{num} is divisible by 11")
if (num%5==0) and (num%11!=0):
    print(f"{num} is divisible by 5")
if (num%5!=0) and (num%11!=0):
    print(f"{num} is not divisible by 5 and 11")


#Q7
num=int(input("Enter number: "))
if (num%3==0) and (num%7==0):
    print(f"{num} is divisible by 3 and 7")
if (num%3!=0) and (num%7==0):
    print(f"{num} is divisible by 7")
if (num%5==0) and (num%7!=0):
    print(f"{num} is divisible by 3")
if (num%3!=0) and (num%7!=0):
    print(f"{num} is not divisible by 3 and 7")

#Q8
marks=int(input("enter your marks: "))
if (marks>100) or (marks<0):
    print("invalid marks")
if marks>=40:
    print("Pass")
if marks<=40:
    print("Fail")

#Q9
marks=int(input("enter marks: "))

if (marks>100) or (marks<0):
    print("invalid marks")
elif (marks>=90) and (marks<100):
    print("A")
elif (marks>=80) and (marks<90):
    print("B")
elif(marks>=70) and (marks<80):
    print("C")
elif(marks>=60) and (marks<70):
    print("D")
elif(marks>=40) and (marks<60):
    print("E")
else:
    print("Fail")


#Q10
age=int(input("enter your age: "))
if age>120:
    print("Too old to vote")
if age>=18:
        (print("eligible to vote"))
elif age<18:
        print("cannot vote")
else:
    print("invalid data")

#Q11
year=int(input("enter year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("it's a leap year")
else:
    print("not a leap year")

#Q12
sample=input("enter data: ")



#Q13

#Q14
cp=int(input("enter your cost price: "))
sp=int(input("enter your selling price: "))

loss=(cp-sp)
profit=(sp-cp)
if cp>sp:
    print("there is loss")
    print(f"loss: {loss}")

elif sp>cp:
    print("there is profit")
    print(f"Profit: {profit}")

elif cp==sp:
    print("no loss no profit")


#Q15
cp=int(input("enter your cost price: "))
sp=int(input("enter your selling price: "))

loss=(cp-sp)
loss_percentage=((cp-sp)/cp*100)

profit=(sp-cp)
profit_percentage=((sp-cp)/cp*100)

if cp>sp:
    print("there is loss")
    print(f"loss: {loss}")
    print(f"loss percent: {loss_percentage}")
elif sp>cp:
    print("there is profit")
    print(f"Profit: {profit_percentage}")

elif cp==sp:
    print("no loss no profit")


#Q16
unit=int(input("enter electricity unit : "))

if unit<=100:
    print("Bill : ",(unit)*5)

elif unit>100:
     print("Bill : ",((unit*100)+((unit-100)*7)))

elif unit>200:
    print("Bill : ",((100*5)+(100*7)+((unit-200)*10)))


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

#Q18
temp=int(input("enter temperature (in celsius): "))

if temp<0:
    print("freezing")
elif temp>=0 and temp<=15:
    print("very cold")
elif temp>15 and temp<=25:
    print("Cold")
elif temp>25 and temp<=35:
    print("Normal")
elif temp>35:
    print("Hot")

#Q19
num=int(input("enter number: "))

if num<0:
    print("Number is negative")
elif num>=0 and num<=10:
    print("Number is between 0 and 10")
elif num>10 and num<=50:
    print("Number is between 10 and 50")
elif num>50 and num<=100:
    print("Number is between 51 and 100")
elif num>100:
    print(" Number is above 100")

#Q20
first_side=int(input("enter first side: "))
second_side=int(input("enter second side: "))
third_side=int(input("enter third side: "))

if (first_side+second_side>third_side) and (second_side+third_side>first_side) and (first_side+third_side>second_side):
    print("triangle can be formed")


#Q21
first_side=int(input("enter first side: "))
second_side=int(input("enter second side: "))
third_side=int(input("enter third side: "))

if (first_side+second_side>third_side) and (second_side+third_side>first_side) and (first_side+third_side>second_side):
    print("triangle can be formed")

    if (first_side==second_side==third_side):
        print("triangle is equilateral")

    elif (first_side==second_side) or (second_side==third_side) or (first_side==third_side):
        print("triangle is isoceles")

    else:
        print("triangle is scalene")

else:
    print("triangle cannot be formed")

    print(f"sides: {first_side},{second_side},{third_side}")

#Q22
acc_balance=int(input("Enter account balance: "))
withdrawal_amount=int(input("Enter withdrawal amount: "))

if acc_balance>withdrawal_amount:
    if withdrawal_amount>0:
        if withdrawal_amount%100==0:
            if (acc_balance-withdrawal_amount)>=500:
                print(f'''withdrawl successful 
                Remaining Balance: {(acc_balance-withdrawal_amount)}''')

#Q23

username=input("enter your username: ")
if username=="admin":
    print("username correct allowed to enter password")
    password=input("enter your password: ")
    if password=="python123":
        print("Login Successful")
    else:
        print("wrong password")
else:
    print("User not found")


#Q24
price=int(input("enter the price: "))

dis_price=(price-(20/100*price))

if price<500:
    print("discount offered - 0%")
    
elif price>=500 and price<1000:
    print("discount offered - 5%")
    print(f''' original price: {price}
    Discount percentage: 5%
    Discount amount {((5/100*price))}
    Final amount: {(price-(5/100*price))}''')

elif price>=1000 and price<2000:
    print("discount offered - 10%")
    print(f''' original price: {price}
    Discount percentage: 10%
    Discount amount {((10/100*price))}
    Final amount: {(price-(10/100*price))}''')

elif price>=2000 and price<5000:
    print("discount offered - 20%")
    print(f''' original price: {price}
    Discount percentage: 20%
    Discount amount {((15/100*price))}
    Final amount: {(price-(15/100*price))}''')

elif price>=5000:
    print("discount offered - 20%")
    print(f''' original price: {price}
    Discount percentage: 20%
    Discount amount {((20/100*price))}
    Final amount: {(price-(20/100*price))}''')

#Q25
sub1=int(input("Enter marks: "))
sub2=int(input("Enter marks: "))
sub3=int(input("Enter marks: "))
average=((sub1+sub2+sub3)/3)

if (sub1>35 and 0<=sub1>=100) and (sub2>35 and 0<=sub2>=100) and (sub3>35 and 0<=sub3>=100):
    if (average>=75):
        print("Distinction")
    elif (average>=60) and (average<75):
        print("First class")
    elif (average>=50) and (average<60):
            print("Second class")
    elif (average>=35) and (average<50):
            print("Pass")
else: 
    print("Fail")

#Q26


#Q27
hour=int(input("Enter hour: "))
minutes=int(input("Enter minutes: "))
seconds=int(input("Enter seconds: "))

if (0<=hour<=23) and (0<=minutes<=59) and (0<=seconds<=59):
    print("Valid Time")
else:
    print("Invalid Time")

#Q28
per_1,age_1=(input,map("Enter first person name and age: ").split())
per_2,age_2=(input,map("Enter second person name and age: ").split())
per_3,age_3=(input,map("Enter third person name and age: ").split())

print(f'''{per_1,age_1}
{per_2,age_2}
{per_3,age_3}''')

if (age_1<age_2) and (age_1<age_3) :
    print(f"{per_1} is the youngest")
elif (age_2<age_1) and (age_2<age_3) :
    print(f"{per_2} is the youngest")
elif (age_3<age_1) and (age_3<age_2) :
    print(f"{per_1} is the youngest")
elif (age_1==age_2) and(age_2==age_3):
    print(f"{per_1} and {per_2} and {per_3} has the same age ")
elif (age_1==age_2):
    print(f"{per_1} and {per_2}have the same age")
elif (age_2==age_3):
    print(f"{per_2} and {per_3} have the same age")
else:
    print(f"{per_1} and {per_3} have the same age")

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

#Q30
age=int(input("Enter age: "))
marks=int(input("Enter marks: "))
family_income=int(input("Enter income: "))
Attendance=int(input("Enter Attendance in(%): "))

if (18<=age<=25) and (85>=marks<100) and (75>=Attendance<100) and family_income>=300000:
    print("Scholarship Approved")
    

















    




