def calculate(a,b):
    sum=a+b
    diff=a-b
    prod=a*b
    div=a/b
    return(f"sum: {sum} diff: {diff} prod: {prod} div: {div}")

m=int(input("enter number: "))
n=int(input("enter number: "))
while(n==0):
    n=int(input("enter number: "))

print(calculate(m,n))