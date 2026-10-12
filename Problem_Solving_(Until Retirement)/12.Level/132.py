n=int(input("enter number: "))
arr=[]

while n>0:
    digit=n%10
    n//=10
    arr.append(digit)

print(min(arr))