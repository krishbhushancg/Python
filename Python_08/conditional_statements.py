#Q1
num=int(input("Enter a number: "))
if num>10:
    print("greater than 10.")

#Q2
age=int(input("Enter your age: "))
if age>=18:
    print("Adult")

#Q3
num=int(input("Enter your number: "))
if num>0:
    print("positive")

#Q4
marks=int(input("enter your marks: "))
if marks>=40:
    print("Pass")

#Q5
num=int(input("Enter a number: "))
if num==0:
    print("Zero")

#Q6
num=int(input("enter your number: "))
if num>0:
    print("positive")
else:
    print("Not Positive")

#Q7
age=int(input("Enter Age: "))
if age>=18:
    print("Adult")
else:
    print("Minor")

#Q8
num=int(input("enter your number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

#Q9
marks=int(input("Enter marks: "))
if marks>=40:
    print("Pass")
else:
    print("Fail")

#Q10
a,b=map(int,input("Enter your numbers: ").split()[:2])
if a>b:
    print("a is bigger")
else:
    print("b is bigger")

#Q11
marks=int(input("enter your marks: "))
if 90<=marks>100:
    print("A")
elif 90<marks>=75:
    print("B")
elif 75<marks>=60:
    print("C")
elif 60<marks>=40:
    print("D")
else:
    print("F")

#Q12
num=int(input("enter your number: "))
if num>0:
    print("Positive")
if num<0:
    print("Negative")
else:
    print("Zero")

#Q13
num=int(input("enter your number: "))
if num==1:
    print("Monday")
if num==2:
    print("Tuesday")
if num==3:
    print("Wednesday")
if num==4:
    print("Thursday")
if num==5:
    print("Friday")
else:
    print("Other")

#Q14
marks=int(input("enter your marks: "))
if 90 <= marks <= 100:
    print("Excellent")
elif 75 <= marks < 90:
    print("Good")
elif 60 <= marks < 75:
    print("Pass")
else:
    print("Fail")

#Q15
num=int(input("enter number: "))
if num==1:
    print("number is 1")
elif num==2:
    print("number is 2")
elif num==3:
    print("number is 3")
else:
    print("other")

#Q16
age=int(input("Enter your age: "))
if age>=18:
    if age<=60:
        print("Between 18 and 60")

#Q17
marks=int(input("enter marks: "))
if marks>=40:
    print("passed")
    
    if marks>=75:
        print("Good")

        if marks<40:
            print("Failed")

#Q18
num=int(input("enter number: "))
if num>=0:
    print("Positive")
    if num<100:
        print("greater than 100")

#Q19
age=int(input("Enter your age: "))
if age>=18:
    print("adult")
    if age>=60:
        print("Adult above 60")

#Q20
num=int(input("enter number"))
if num!=0:
    print("number is a non zero")
    if num<0:
        print("negative")
        if num>0:
            print("positive")

#Q21
age,marks=map(int,input("enter age and marks").split()[:2])
if age>=18 and marks>=40:
    print("eligible")
else:
    print("Not eligible")

#Q22
num=int(input("Enter number: "))
if num<10 or num>100:
    print("Special")

#Q23
age=int(input("Enter age: "))
has_id=bool(input("Enter your id"))
if age>=18 and has_id==True:
    print("Allowed")

#Q24
num1,num2=int(input("Enter both number; ").split())
if num1>10 and num2>10:
    print("Both are greater than 10")

#Q25
num=int(input("Enter number: "))
if num>0 or num<100:
    print("number is either less than 0 or greater than 100")
else:
    print("number is between 0 and 100")


#Q26
is_closed=bool(input("enter opened or closed: "))
if not(is_closed==False):
    print("open")

#Q27
num=int(input("enter number: "))
if num>10 and num<50:
    print("number is between 10 and 50")
else:
    print("number is not between 10 and 50")

#Q28
num=int(input("enter number: "))
if num<10 or num>50:
    print("number is outside 10 and 50")

#Q29
is_student=bool(input("enter student id: "))
has_id=bool(input("enter id status: "))
has_ticket=bool(input("enter ticket id: "))

if is_student==True and has_id==True and has_ticket==True:
    print("Allowed")
else:
    print("not allowed")

#Q30
age=int(input("enter your age: "))
marks=int(input("enter marks: "))                           #And is suitable for this question because we have 
has_id=bool(input("enter id status: "))                     # to check every condition and verify all to display the result

if age>=18 and marks>=40 and has_id==True:
    print("Eligible")
else:
    print("Not Eligible")

