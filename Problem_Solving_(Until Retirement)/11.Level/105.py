def odd(number):
    if number%2!=0:
        return(True)
    else:
        return(False)

n=int(input("enter number: "))
print(odd(n))