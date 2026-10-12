n=int(input("enter number 1: "))
m=int(input("enter number 2: "))
gcd=1

for i in range(1,min(n,m)+1):
    if n%i==0 and m%i==0:
        gcd=i

if gcd==1:
    print(True)
else:
    print(False)