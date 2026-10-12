def c_f (C):
    F = (C * 9/5) + 32
    return(F)

n=int(input("enter celsius: "))
print(c_f(n))