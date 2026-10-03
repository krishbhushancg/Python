a=int(input("enter number: "))
b=int(input("enter number: "))
c=int(input("enter number: "))
if a>b and a>c:
    print(f"greater: {a}")
elif b>a and b>c:
    print(f"greater: {b}")
elif c>a and c>b:
    print(f" greater {c}")
else:
    print(f"all are equal")