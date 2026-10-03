n=int(input("enter number: "))
count=0

while n>0:
    digit=n%10
    count+=1
    n//=10

print(f"count: {count}")