n=int(input("enter number: "))

while n<10 or n>50:
    n=int(input("enter number: "))

if n%2==0:
    print(n,"even number")
else:
    print(n,"odd number")