def bet(number):
    if number>=1 and number<=100:
        return(True)
    else:
        return(False)

n=int(input("enter number: "))
print(bet(n))