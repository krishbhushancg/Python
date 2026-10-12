def f_c (F):
    C = (F - 32)* 5/9
    return(C)

n=int(input("enter fahrenheit: "))
print(f_c(n))