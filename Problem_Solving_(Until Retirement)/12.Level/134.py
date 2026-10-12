n=int(input("enter number: "))
arr=[]
odd=0

while n>0:
    digit=n%10
    n//=10
    arr.append(digit)

for i in arr:
    if i%2!=0:
        odd+=1

print(f"odd numbers: {odd}")