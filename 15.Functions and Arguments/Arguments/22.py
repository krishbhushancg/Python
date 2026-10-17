def calculate_stats(a, b, c):
    maximum=(max(a,b,c))
    minimum=(min(a,b,c))
    sum=(a+b+c)
    return(maximum,minimum,sum)


n=int(input("enter number: "))
m=int(input("enter number: "))
o=int(input("enter number: "))

print(calculate_stats(n,m,o))