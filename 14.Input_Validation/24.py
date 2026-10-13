balance=10000

n=int(input("enter withdrawal amount: "))
while n<0 or n>balance or n%100!=0:
    n=int(input("enter withdrawal amount: "))

balance-=n
print(f"current balnce: {balance}")