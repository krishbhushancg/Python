n=int(input("enter number: "))
original=n
sum=0

while n>0:
    digit=n%10
    sum+=digit
    n//=10

if (original%sum==0):
    print(True)
else:
    print(False)