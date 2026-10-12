n=input("enter string: ") 

s=len(n)

middle=s//2

if s%2==0:
    print(n[middle-1: middle+1])
else:
    print(n[middle])