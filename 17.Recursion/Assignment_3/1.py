n=int(input("enter number: "))
m=input("enter message: ")

def printer(n,m):
    if n==0:
        return

    print(m)
    printer(n-1,m)

(printer(n,m))