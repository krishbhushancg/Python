a=int(input("enter number: "))

def max_digit(n):
    if n<10:
        return n

    last=n%10
    rest=max_digit(n//10)

    if last>rest:
        return(last)
    else:
        return(rest)


print(max_digit(a))