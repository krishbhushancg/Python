n=int(input("enter number: "))
m=int(input("enter number: "))

small = lambda a,b: a if a<b else b

print(small(n,m))