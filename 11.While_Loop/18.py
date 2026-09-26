n=int(input("enter number: "))
a=0
i=1
while i<=n:
    if i%2!=0:
        a+=i
    i+=1
print(f"sum: {a}")