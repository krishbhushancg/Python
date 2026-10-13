n=int(input("enter marks: "))

while n<0 or n>100:
    n=int(input("enter marks: "))

if n>75:
    print("Distinction")
elif n>60:
    print("First Class")
elif n>=35:
    print("Pass")
else:
    print("Fail")