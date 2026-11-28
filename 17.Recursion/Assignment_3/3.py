n=int(input("enter number: "))
sum=0 

def sum_odd(n):
    global sum

    if n==0:
        return sum

    if n%2!=0:
        sum+=n

    return sum_odd(n-1)

print(sum_odd(n))