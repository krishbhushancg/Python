print('''+ -> 1
- -> 2
* -> 3
/ -> 4''')

n=int(input("enter operation number: "))

while n<0 or n>4:
    n=int(input("enter operation number: "))

a=int(input("enter number 1: "))
b=int(input("enter number 2: "))

if n==1:
    print(a+b)
elif n==2:
    print(a-b)
elif n==3:
    print(a*b)
elif n==4:
    if b==0:
        while b==0:
            print("try again")
            b=int(input("enter number 2: "))
        print(a/b)