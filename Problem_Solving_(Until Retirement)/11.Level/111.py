def long(a,b):
    if len(a)>len(b):
        return(a)
    elif len(a)==len(b):
        return(a)
    else:
        return(b)


p=input("enter string 1: ")
n=input("enter string 2: ")

print(long(n,p))