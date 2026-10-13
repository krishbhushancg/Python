n=input("enter name: ").strip()

while len(n)<5 or n==0 or " " in n:
    n=input("enter name: ").strip()

print("username:",n)