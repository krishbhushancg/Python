#Q25
sub1=int(input("Enter marks: "))
sub2=int(input("Enter marks: "))
sub3=int(input("Enter marks: "))
average=((sub1+sub2+sub3)/3)


if ((sub1>100) or (sub1<0)) or ((sub2>100) or (sub2<0)) or ((sub3>100) or (sub3<0)):
     print("Invalid marks")
elif sub1<35 or sub2<35 or sub3<35: 
    print("Fail")

else:
    if (average>=75) and average<=100:
        print("Distinction")
    elif (average>=60) and (average<75):
        print("First class")
    elif (average>=50) and (average<60):
            print("Second class")
    elif (average>=35) and (average<50):
            print("Pass")