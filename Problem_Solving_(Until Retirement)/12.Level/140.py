n=int(input("enter number: "))
square=n**2

digit=square%10

if digit==n:
    print(True)
else:
    print(False)