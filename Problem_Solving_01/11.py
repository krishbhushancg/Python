#Q11
year=int(input("enter year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("it's a leap year")
else:
    print("not a leap year")

