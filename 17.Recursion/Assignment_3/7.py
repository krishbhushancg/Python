n=int(input("enter number: "))
t=int(input("enter target: "))

res=False

def check_digit(n):
    global res
    if n<10:
        if n==t:
            res=True
        return res
    
    if n%10==t:
        res=True

    return(check_digit(n//10))


print(check_digit(n))