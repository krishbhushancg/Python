def sign(a):
    if (a>0):
        return("positive")
    elif (a<0):
        return("negative")
    else:
        return("zero")


n=int(input("enter number 1 : "))

print(sign(n))