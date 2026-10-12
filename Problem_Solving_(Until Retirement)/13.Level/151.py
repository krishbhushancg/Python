n=input("enter text: ").split()
smallest=len(n[0])

for i in n:
    if len(i)<smallest:
        smallest=len(i)

print(smallest)