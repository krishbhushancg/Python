n=int(input("enter a number: "))

if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(f"{n} is not prime number")
            break
        else:
            print(f"{n} is a prime number")
else:
    ("not prime number")
