n=int(input("enter number: "))

prod=1

def product(n):
    global prod
    if n==0:
        return prod

    prod *= n%10

    return(product(n//10))

print(product(n))