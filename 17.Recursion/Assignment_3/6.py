n=int(input("enter number: "))


def first(n):
    if n<10:
        return n

    return(first(n//10))

print(first(n))