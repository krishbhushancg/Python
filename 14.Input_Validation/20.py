n=int(input("number of values: "))
while n<1:
    n=int(input("number of values: "))

sum=0
for i in range(n):
    m=int(input("enter number: "))
    while m<0 or m>20:
        m=int(input("enter number: "))
    sum +=m

average=sum/n
print(f"average: {average}")