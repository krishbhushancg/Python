n=int(input("enter number: "))
m=int(input("enter number: "))

greater = lambda a,b: a if a>b else b

print(greater(n,m))