n=int(input("enter number: "))

def even_printer(n):
    if n<2:
        return

    (even_printer(n-1))

    if n%2==0:
        print(n)

even_printer(n)