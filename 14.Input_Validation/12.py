balance=2000
n=int(input("enter deposit amount: "))

while n<0 :
    print("try again!")
    n=int(input("enter deposit amount: "))

balance+=n
print(f"updated balance: {balance}")