#Q30
age=int(input("Enter age: "))
marks=int(input("Enter marks: "))
family_income=int(input("Enter income: "))
Attendance=int(input("Enter Attendance in(%): "))

if ((18<=age<=25) and (85<=marks<100) and (75<=Attendance<100) and (family_income<=300000)):
    print("Scholarship Approved")
else:
    print("scholarship not approved")