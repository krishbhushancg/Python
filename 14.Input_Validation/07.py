balance=5000
n=int(input("enter withdrawal amount: "))

while n<0 or n>balance or n==0:
    print("try again!")
    n=int(input("enter withdrawal amount: "))

balance-=n
print(f"remaining balance: {balance}")