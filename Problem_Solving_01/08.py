#Q8
marks=int(input("enter your marks: "))
if (marks>100) or (marks<0):
    print("invalid marks")
elif marks>=40:
    print("Pass")
else:
    print("Fail")